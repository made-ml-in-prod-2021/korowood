import logging
import os

import pandas as pd
import uvicorn
from typing import List, Any
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from .entities import DiagnosisResponse, DiagnosisRequest

DEFAULT_VALIDATION_ERROR_CODE = 400

logging.basicConfig(filename="app.log", level=logging.DEBUG)
logger = logging.getLogger(__name__)
model: Any = None
app = FastAPI()


@app.get("/")
async def main():
    return "it is entry point of our predictor"


@app.on_event("startup")
def load_model():
    logger.info(f"Loading model...")
    global model
    path = os.getenv("MODEL_PATH")
    if path is None:
        path = os.path.join('model', 'model.pkl')
    model = pd.read_pickle(path)

    logger.info(f"Model loaded.")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    # print(str(exc))
    return PlainTextResponse(str(exc), status_code=DEFAULT_VALIDATION_ERROR_CODE)


@app.post("/predict", response_model=List[DiagnosisResponse])
def predict(request: DiagnosisRequest):
    return predict_(request.data, request.features)


def predict_(data: List, features: List[str]) -> List[DiagnosisResponse]:
    global model
    data = pd.DataFrame(data, columns=features)
    # print(data)
    pred = model.predict(data)
    result = [
        DiagnosisResponse(id=tp[0], diagnosis=tp[1])
        for tp in enumerate(pred)
    ]
    return result


if __name__ == "__main__":
    uvicorn.run("src.app:app", host="localhost", port=os.getenv("PORT", 8000))
