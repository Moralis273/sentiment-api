from fastapi import FastAPI
from pydantic import BaseModel,Field
from app.services.inference import InferenceService
from app.config import THRESHOLD,MODEL_NAME,MAX_TEXT_LENGTH
from app.schemas.sentiment import PredictRequest,PredictResponse
import time
import uuid
import logging


logging.basicConfig(level=logging.INFO)

app=FastAPI()
     
inference_service=InferenceService()

@app.get("/")
def root():
     return {"message":"API is running"}

@app.get("/health")
def health():
     return {"status":"ok"}

@app.post("/predict",response_model=PredictResponse)
def predict(request:PredictRequest):
     result=inference_service.predict(request.text)
     return result
