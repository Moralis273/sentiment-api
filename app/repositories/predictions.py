from app.database import get_conn


def save_predictions(
     request_id: str,
     text: str,
     label: str,
     score: float,
     processing_time_ms: float) -> None:
     conn=get_conn()
     curr=conn.cursor()
     query="""INSERT INTO predictions (request_id,text,label,score,processing_time_ms
               )
               VALUES (%s,%s,%s,%s,%s)"""
     values=(request_id,text,label,score,processing_time_ms)
     curr.execute(query=query,vars=values)
     conn.commit()
     curr.close()
     conn.close()
