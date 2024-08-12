import psycopg2
import logging
import os 
from dotenv import load_dotenv
load_dotenv()
def db_connect():
    try:
        conn = psycopg2.connect(database=os.getenv("databa"), host=os.getenv("hostme"), user=os.getenv("userme"), password=os.getenv("pass") ,port=os.getenv("POST"))
        return conn
    except Exception as e:
        logging.info(f"connecting error: {e}")
        raise ValueError(f"connecting error: {e}")
    
def get_all_users():
        try:
            conn=db_connect()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users")
                users = cursor.fetchall()
                return users
        except Exception as e:
            logging.info(f"error getting all users: {e}")
        finally:
            conn.close()

def create_user(data):
        try:
            conn=db_connect()
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO users (name, password) VALUES (%s, %s)",(data.name,data.password))
                conn.commit()
        except Exception as e:
            logging.info(f"creating user error: {e}")
        finally:
            conn.close()

def delete_user(user_id):
        try:
            conn=db_connect()
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE id = %s", (user_id))
                conn.commit()
        except Exception as e:
            logging.info(f"delete user error: {e}")
        finally:
            conn.close()

def update_user(data):
        try:
            conn=db_connect()
            with conn.cursor() as cursor:
                cursor.execute(
                        "UPDATE users SET name = %s, password = %s WHERE id = %s",
                        (data.name,data.password, data.id)
                    )
                conn.commit()
        except Exception as e:
            logging.info(f"update user error {e}")
        finally:
            conn.close()


def get_user(user_id):
        try:
            conn=db_connect()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users where id = %s",(user_id))
                user = cursor.fetchall()
                return user
        except Exception as e:
            logging.info(f"error user by id: {e}")
        finally:
            conn.close()

