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

def get_recent_prediction(limit: int):
     conn=get_conn()
     curr=conn.cursor()
     query="""SELECT 
          request_id, text, label, score, processing_time_ms, created_at
     FROM predictions ORDER BY created_at DESC LIMIT %s"""
     vars=(limit,)
     curr.execute(query=query,vars=vars)
     rows=curr.fetchall()
     curr.close()
     conn.close()
     
     result=[]
     
     for row in rows:
          result.append(
               {
                "request_id": row[0],
                "text": row[1],
                "label": row[2],
                "score": row[3],
                "processing_time_ms": row[4],
                "created_at": row[5],
               }
          )
     return result
          
def save_predictions_zero_shot(
                              request_id: str,
                              text: str,
                              result_label: str,
                              score: float,
                              processing_time_ms: float) -> None :
     conn=get_conn()
     curr=conn.cursor()
     query="""INSERT INTO zero_shut_table (request_id,text,result_label,score,processing_time_ms) 
               VALUES (%s,%s,%s,%s,%s)"""
     vars=(request_id,text,result_label,score,processing_time_ms)
     curr.execute(query=query,vars=vars)
     conn.commit()
     curr.close()
     conn.close()
     



