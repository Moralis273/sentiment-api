from pydantic import BaseModel,Field
from app.config import MAX_TEXT_LENGTH
from datetime import datetime

class PredictRequest(BaseModel):
     text: str =Field(...,min_length=1,max_length=MAX_TEXT_LENGTH)

class PredictResponse(BaseModel):
     text: str
     label: str
     score: float
     request_id: str
     processing_time_ms: float
     
class PredictionHistoryItem(BaseModel):
     request_id: str
     text: str 
     label: str 
     score: float 
     processing_time_ms: float 
     created_at: datetime
     
class ZeroShotRequest(BaseModel):
     text: str
     candidate_labels: list[str]
     
class ZeroShotResponse(BaseModel):
     request_id: str
     text: str 
     label: str 
     score: float 
     processing_time_ms: float 