from flask import Blueprint, abort, request, jsonify

routes_image = Blueprint("image", __name__)


images = {
    1: {"url": "https://example.com/image1.jpg", "description": "Beautiful landscape"},
    2: {"url": "https://example.com/image2.jpg", "description": "City skyline"},
}


@routes_image.route("/images", methods=["GET"])
def get_images():
    try:
        # TODO Using crud operations of the DB
        return jsonify(images)
    except FileNotFoundError as error:
        abort(404, error)
    except Exception as error:
        abort(400, error)


@routes_image.route("/images/<int:image_id>", methods=["GET"])
def get_image(image_id):
    try:
        # TODO Using crud operations of the DB
        image = images.get(image_id)
        if image:
            return jsonify(image)
        return jsonify({"message": "Image not found"}), 404
    except FileNotFoundError as error:
        abort(404, error)
    except Exception as error:
        abort(400, error)


@routes_image.route("/images", methods=["POST"])
def create_image():
    try:
        # TODO Using crud operations of the DB
        new_image = request.json
        image_id = len(images) + 1
        images[image_id] = new_image
        return jsonify({"id": image_id}), 201
    except FileNotFoundError as error:
        abort(404, error)
    except Exception as error:
        abort(400, error)


@routes_image.route("/images/<int:image_id>", methods=["PUT"])
def update_image(image_id):
    try:
        # TODO Using crud operations of the DB
        updated_image = request.json
        if image_id in images:
            images[image_id] = updated_image
            return jsonify({"message": "Image updated"})
        else:
            return jsonify({"message": "Image not found"}), 404  # chack
    except FileNotFoundError as error:
        abort(404, error)
    except Exception as error:
        abort(400, error)
