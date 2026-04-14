from flask import Blueprint, request, jsonify
from config.db import faq

faq_routes = Blueprint("faq_routes", __name__)

# ADD FAQ
@faq_routes.route("/add", methods=["POST"])
def add_faq():
    data = request.json

    faq.insert_one({
        "question": data.get("question"),
        "answer": data.get("answer")
    })

    return jsonify({"message": "FAQ added"})


# GET FAQ
@faq_routes.route("/", methods=["GET"])
def get_faq():
    data = []

    for f in faq.find():
        data.append({
            "_id": str(f["_id"]),
            "question": f.get("question"),
            "answer": f.get("answer")
        })

    return jsonify(data)