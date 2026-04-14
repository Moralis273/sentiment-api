from pydantic import BaseModel,Field
from app.config import MAX_TEXT_LENGTH

class PredictRequest(BaseModel):
     text: str =Field(...,min_length=1,max_length=MAX_TEXT_LENGTH)

class PredictResponse(BaseModel):
     text: str
     label: str
     score: float
     uuid: str
     processing_time_ms: float