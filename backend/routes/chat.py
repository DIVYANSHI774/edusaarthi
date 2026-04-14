from flask import Blueprint, request, jsonify
from services.chatbot_service import get_answer

chat_routes = Blueprint("chat_routes", __name__)

@chat_routes.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        message = data.get("message", "")

        if not message:
            return jsonify({"reply": "No message received"}), 400

        response = get_answer(message)

        return jsonify({"reply": response})

    except Exception as e:
        return jsonify({"reply": "Server error", "error": str(e)}), 500