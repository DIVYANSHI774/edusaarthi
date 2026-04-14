from flask import request, jsonify
from utils.jwt_handler import verify_token
from config.db import users_collection

def get_current_user():
    auth = request.headers.get("Authorization")

    if not auth:
        return None

    try:
        token = auth.split(" ")[1]
        data = verify_token(token)
        return users_collection.find_one({"username": data["username"]})
    except:
        return None