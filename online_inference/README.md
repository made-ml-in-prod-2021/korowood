HW2
==============================

##Python:

run app: from online_inference

    python -m src.app

curl:

     curl -X 'POST'   'http://localhost:8000/predict'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
      "data": [[0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]],
      "features": ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang",
                "oldpeak", "slope", "ca", "thal"]}'

------------
##Docker

build:

    docker build -t model_inference:v1 .
run:

    docker run --network host model_inference:v1

docker.hub:

pull:

    docker pull korowood/model_inference:v1

run:
    
    docker run --network host korowood/model_inference:v1

push:

    docker push korowood/online_inference:v1

--------



