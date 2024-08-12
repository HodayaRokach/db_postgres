from flask import Flask
from init_db import init_db_func

app = Flask(__name__)
init_db_func()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    