from dotenv import load_dotenv
import os



load_dotenv()

MODEL_NAME=os.getenv("MODEL_NAME","seara/rubert-tiny2-russian-sentiment")
THRESHOLD=float(os.getenv("THRESHOLD","0.65"))
MAX_TEXT_LENGTH=int(os.getenv("MAX_TEXT_LENGTH","100"))
ZERO_SHOT_MODEL=os.getenv("ZERO_SHOT_MODEL","facebook/bart-large-mnli")
#wh
DB_HOST=os.getenv("DB_HOST")
DB_PORT=int(os.getenv("DB_PORT"))
DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")

