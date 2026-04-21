from transformers import pipeline
from app.config import THRESHOLD,MODEL_NAME,ZERO_SHOT_MODEL
import time
import uuid
import logging
import numpy as np

logger=logging.getLogger(__name__)

class InferenceService():
     def __init__(self):
          self.classifier =pipeline("sentiment-analysis",model=MODEL_NAME)
          self.threshold=THRESHOLD
     def predict(self,text:str):
          request_id=str(uuid.uuid4())
          logger.info("Received prediction request: request_id=%s text=%s",request_id,text)
          t1=time.perf_counter()
          result=self.classifier(text)[0]
          label=result['label'].lower()
          score=round(float(result['score']),3)
          t2=time.perf_counter()
          if score<self.threshold:
               label='neutral'
          dt=round((t2-t1)*1000,3)
          logger.info("Prediction completed:: request_id=%s label=%s score=%.3f processing_time_ms=%.3f",request_id,label,score,dt)
          return {"text":text,
                  "label":label,
                  "score":score,
                  "request_id":request_id,
                  "processing_time_ms":dt}
          
class ZeroShotInference():
     def __init__(self):
          self.classifier=pipeline("zero-shot-classification",model=ZERO_SHOT_MODEL)
     def predict(self,text:str,candidate_labels:list[str]):
          request_id=str(uuid.uuid4()) 
          logger.info("Received zero_shot_pred_request: request_id=%s text=%s",request_id,text)   
          t1=time.perf_counter()
          result=self.classifier(text,candidate_labels)
          result_label=result['labels'][0]
          score=round(result['scores'][0],2)
          t2=time.perf_counter()
          dt=round((t2-t1)*1000,3)
          logger.info("Prediction completed: request_id=%s label=%s score=%.3f processing_time_ms=%.3f",request_id,result_label,score,dt)
          return {"text":text,
                  "label":result_label,
                  "score":score,
                  "request_id":request_id,
                  "processing_time_ms":dt}
