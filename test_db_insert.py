from app.database import get_conn
from app.config import DB_HOST,DB_PORT,DB_NAME,DB_USER,DB_PASSWORD,POSTGRES_USER
from app.repositories.predictions import save_predictions

     
#conn=get_conn()#DB_HOST,DB_PORT,DB_NAME,DB_USER,DB_PASSWORD,POSTGRES_USER)
#curr=conn.cursor()
#curr.execute("""INSERT INTO predictions (request_id,text,label,score,processing_time_ms
#             )
#             VALUES (%s,%s,%s,%s,%s)""",
#             ['901','Привет все крутао','positive',0.99, 54])
#conn.commit()
#curr.close()
#conn.close()
#

def test_save():
     save_predictions(request_id='999',
                      text='нихау епта',
                      label='positive',
                      score=0.89,
                      processing_time_ms=50)
     
if __name__=='__main__':
     test_save()