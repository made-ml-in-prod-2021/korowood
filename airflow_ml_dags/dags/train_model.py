from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.filesystem import FileSensor
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "02_train_model",
        default_args=default_args,
        schedule_interval="@weekly",
        start_date=days_ago(1),
) as dag:
    wait_for_data = FileSensor(
        task_id='wait-for-data',
        poke_interval=10,
        retries=5,
        filepath="data/raw/{{ ds }}/data.csv",
        # filepath="data/raw/data.csv",
    )
    wait_for_target = FileSensor(
        task_id='wait-for-target',
        poke_interval=10,
        retries=5,
        filepath="data/raw/{{ ds }}/target.csv",
        # filepath="data/raw/target.csv",
    )
    preprocess = DockerOperator(
        image="korowood/airflow-preprocess",
        command="--input-dir /data/raw/{{ ds }} --output-dir /data/processed/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-preprocess",
        do_xcom_push=False,
        volumes=["/home/dm/Документы/MADE/2 семетстр/korowood/airflow_ml_dags/data:/data"]
    )

    split = DockerOperator(
        image="korowood/airflow-split",
        command="--input-dir /data/processed/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-split",
        do_xcom_push=False,
        volumes=["/home/dm/Документы/MADE/2 семетстр/korowood/airflow_ml_dags/data:/data"]
    )

    train = DockerOperator(
        image="korowood/airflow-train",
        command="--input-dir /data/processed/{{ ds }} --output-dir /data/models/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-train",
        do_xcom_push=False,
        volumes=["/home/dm/Документы/MADE/2 семетстр/korowood/airflow_ml_dags/data:/data"]
    )

    validate = DockerOperator(
        image="korowood/airflow-validate",
        command="--input-dir /data/processed/{{ ds }} \
         --model-dir /data/models/{{ ds }} --output-dir /data/metrics/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-validate",
        do_xcom_push=False,
        volumes=["/home/dm/Документы/MADE/2 семетстр/korowood/airflow_ml_dags/data:/data"]
    )

    [wait_for_data, wait_for_target] >> preprocess >> split >> train >> validate
