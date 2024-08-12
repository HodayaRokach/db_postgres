from flask import abort, request, jsonify, Blueprint

routes_user = Blueprint("user", __name__)


users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
}


@routes_user.route("/users", methods=["GET"])
def get_users():
    try:
        # TODO Using crud operations of the DB
        all_users = get_all_users()
        return jsonify(all_users)
    except FileNotFoundError as error:
        abort(404, error)
    except Exception as error:
        abort(400, error)


@routes_user.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    try:
        # TODO Using crud operations of the DB
        user = get_user(user_id)
        return jsonify(user)
    except Exception as e:
        return jsonify({"error": str(e)}), 404


@routes_user.route("/users", methods=["POST"])
def create_user():
    try:
        # TODO Using crud operations of the DB
        user = request.json
        user_id = len(users) + 1
        users[user_id] = user
        return jsonify({"id": user_id}), 201
    except FileNotFoundError as error:
        abort(404, error)
    except Exception as error:
        abort(400, error)


@routes_user.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        # TODO Using crud operations of the DB
        user = request.json
        if user_id in users:
            users[user_id] = user
            return jsonify({"message": "User updated"})
        else:
            raise Exception(f"User with id {user_id} not found")
    except FileNotFoundError as error:
        abort(404, error)
    except Exception as error:
        abort(400, error)


def get_all_users():
    try:
        return users
    except Exception as e:
        raise Exception(f"Failed to fetch users: {str(e)}")


def get_user(user_id):
    try:
        user = users.get(user_id)
        if user:
            return user
        else:
            raise Exception(f"User with id {user_id} not found")
    except Exception as e:
        raise Exception(f"Failed to fetch user: {str(e)}")
