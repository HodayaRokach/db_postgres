import psycopg2
import os 
from dotenv import load_dotenv

def init_db_func():
    load_dotenv()
    connect = psycopg2.connect(database=os.getenv("databa"), host=os.getenv("hostme"), user=os.getenv("userme"), password=os.getenv("pass") ,port=os.getenv("POST"))
    cur = connect.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users(id serial PRIMARY KEY,name varchar(100), password varchar(100))''')
    cur.execute('''CREATE TABLE IF NOT EXISTS images(id serial PRIMARY KEY,userid integer, image_name varchar(100), image_before_processing bytea, image_after_processing bytea )''')
    connect.commit()
    cur.close()
    connect.close()



