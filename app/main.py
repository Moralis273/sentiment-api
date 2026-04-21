from fastapi import FastAPI,Query,HTTPException
from app.services.inference import InferenceService,ZeroShotInference
from app.schemas.sentiment import PredictRequest,PredictResponse,PredictionHistoryItem,   ZeroShotRequest,ZeroShotResponse
import logging
from app.repositories.predictions import save_predictions,get_recent_prediction,save_predictions_zero_shot
from app.database import get_conn
from fastapi.responses import JSONResponse

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
app=FastAPI()
     
inference_service=InferenceService()
zero_shot_service=ZeroShotInference()


@app.get("/")
def root():
     return {"message":"API is running"}

@app.get("/health")
def health():
     try:
          conn=get_conn()
          curr=conn.cursor()
          query="""SELECT 1;"""
          curr.execute(query)
          curr.close()
          conn.close()
          return {"status":"ok",
               "database":"ok"}
     except Exception:
          logger.exception('Database connection is Failed')
          return JSONResponse(status_code=502,
                             content={"status":"degraded",
                                        "database":"error"})

@app.post("/predict",response_model=PredictResponse)
def predict_sentiment(request:PredictRequest):
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
     
@app.get("/predictions",response_model=list[PredictionHistoryItem])
def get_last_pred(limit: int=Query(10,ge=1,le=100)):
     result=get_recent_prediction(limit)
     return result


@app.post("/predict/zero_shot",response_model=ZeroShotResponse)
def predict_zero_shot(request:ZeroShotRequest):
     result=zero_shot_service.predict(request.text,request.candidate_labels)
     try:
          save_predictions_zero_shot(
                              request_id=result['request_id'],
                              text=result['text'],
                              result_label=result['label'],
                              score=result['score'],
                              processing_time_ms=result['processing_time_ms'])
     except    Exception:
          logger.exception("Failed to save prediction to database: request_id=%s",   result["request_id"])
     return result