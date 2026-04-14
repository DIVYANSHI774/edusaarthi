from flask import Blueprint, request, jsonify
from config.db import db   # ✅ FIXED

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        # 🔍 Find user
        user = db.users.find_one({"username": username})

        if not user:
            return jsonify({"error": "User not found"}), 404

        # 🔐 SIMPLE PASSWORD CHECK (no hashing for now)
        if user["password"] == password:
            return jsonify({
                "message": "Login success",
                "role": user["role"]
            }), 200

        return jsonify({"error": "Invalid password"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500