import psycopg2
from config import DB_HOST,DB_PORT,DB_NAME,DB_USER,DB_PASSWORD,POSTGRES_USER

def get_conn(DB_HOST,DB_PORT,DB_NAME,DB_USER,DB_PASSWORD,POSTGRES_USER):
     conn=psycopg2.connect(host=DB_HOST,
                           port=DB_PORT,
                           dbname=DB_NAME,
                           user=DB_USER,
                           password=DB_PASSWORD,)
     return conn