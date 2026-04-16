from fastapi import FastAPI
from app.services.inference import InferenceService
from app.schemas.sentiment import PredictRequest,PredictResponse
import logging
from app.repositories.predictions import save_predictions

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
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
     try:
          save_predictions(request_id=result["request_id"],
                           text=result["text"],
                           label=result["label"],
                           score=result["score"],
                           processing_time_ms=result["processing_time_ms"])
          
     except Exception:
          logger.exception("Failed to save prediction to database: request_id=%s",   result["request_id"])
     return result
     

#uvicorn app.main:app --reload