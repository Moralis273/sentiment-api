from transformers import pipeline
from app.config import THRESHOLD,MODEL_NAME
import time
import uuid
import logging


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
          dt=(t2-t1)*1000
          logger.info("Prediction completed:: request_id=%s label-%s score=%.3f proccesing_time_ms=%.3f",request_id,label,score,dt)
          return {"text":text,
                  "label":label,
                  "score":score,
                  "uuid":request_id,
                  "processing_time_ms":dt}