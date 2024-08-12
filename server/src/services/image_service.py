import psycopg2
import logging
import os 
from dotenv import load_dotenv
load_dotenv()

def db_connect():
    try:
        conn =psycopg2.connect(database=os.getenv("databa"), host=os.getenv("hostme"), user=os.getenv("userme"), password=os.getenv("pass") ,port=os.getenv("POST"))
        return conn
    except Exception as e:
        logging.info(f"connecting error: {e}")
        raise ValueError(f"connecting error: {e}")
  
    
def get_all_images():
        try: 
            conn = db_connect()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM images")
                images = cursor.fetchall()
                return images
        except Exception as e:
            logging.info(f"error getting all images: {e}")
        finally:
            conn.close()

def create_image(data):
        try:
            conn=db_connect()
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO images (userid, image_name,image_before_processing,image_after_processing) VALUES (%s, %s, %s, %s)",(data.userid,data.image_name,psycopg2.Binary(data.image_before_processing),psycopg2.Binary(data.image_after_processing)))
                conn.commit()
        except Exception as e:
            logging.info(f"creating image error: {e}")
        finally:
            conn.close()

def delete_image(image_id):
        try:
            conn=db_connect()
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM images WHERE id = %s", (image_id))
                conn.commit()
        except Exception as e:
            logging.info(f"delete image error: {e}")
        finally:
            conn.close()

def update_image(data):
        try:
            conn=db_connect()
            with conn.cursor() as cursor:
               cursor.execute(
                        "UPDATE images SET userid = %s, image_name = %s, image_before_processing = %s ,image_after_processing = %s WHERE id = %s",
                        (data.userid,data.image_name,psycopg2.Binary(data.image_before_processing),psycopg2.Binary(data.image_after_processing), data.id)
                    )
               conn.commit()
        except Exception as e:
            logging.info(f"update image error {e}")
        finally:
            conn.close()


def get_image(image_id):
        try:
            conn=db_connect()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM images where id = %s",(image_id))
                user = cursor.fetchall()
                return user
        except Exception as e:
            logging.info(f"error image by id: {e}")
        finally:
            conn.close()