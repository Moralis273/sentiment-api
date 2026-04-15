from app.database import get_conn
from config import DB_HOST,DB_PORT,DB_NAME,DB_USER,DB_PASSWORD,POSTGRES_USER


     
conn=get_conn(DB_HOST,DB_PORT,DB_NAME,DB_USER,DB_PASSWORD,POSTGRES_USER)
curr=conn.cursor()
curr.execute("""INSERT INTO predictions (request_id,text,label,score,processing_time_ms
             )
             VALUES (%s,%s,%s,%s,%s)""",
             ['889','Привет все крутао','positive',0.99, 54])
conn.commit()
curr.close()
conn.close()


