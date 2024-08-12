from flask import Flask
from flask_cors import CORS
from waitress import serve
from init_db import init_db_func
from routers.user_router import routes_user
from routers.image_router import routes_image
init_db_func()
app = Flask(__name__)
CORS(app)

app.register_blueprint(routes_user)
app.register_blueprint(routes_image)


@app.route("/api")
def index():
    return "Image-Reduction"


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
