FROM python:3.8-slim
COPY requirements_tmp.txt ./

RUN pip install -r requirements_tmp.txt

COPY model/ ./model
COPY src/ ./src

EXPOSE 8000

ENV MODEL_PATH="/model/model.pkl"

WORKDIR .
CMD ["uvicorn", "src.app:app"]