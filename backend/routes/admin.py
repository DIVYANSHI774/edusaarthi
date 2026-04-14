from flask import Blueprint, request, jsonify
from config.db import db

admin_routes = Blueprint("admin_routes", __name__)

# ✅ ADD NOTICE
@admin_routes.route("/add-notice", methods=["POST"])
def add_notice():
    data = request.get_json()

    db.notices.insert_one({
        "title": data.get("title"),
        "content": data.get("content")
    })

    return jsonify({"message": "Notice added successfully"}), 200


# ✅ ADD STUDY MATERIAL
@admin_routes.route("/add-study", methods=["POST"])
def add_study():
    data = request.get_json()

    db.study_material.insert_one({
        "title": data.get("title"),
        "content": data.get("content")
    })

    return jsonify({"message": "Study material added successfully"}), 200


# ✅ GET NOTICES
@admin_routes.route("/notices", methods=["GET"])
def get_notices():
    notices = list(db.notices.find({}, {"_id": 0}))
    return jsonify(notices)


# ✅ GET STUDY
@admin_routes.route("/study", methods=["GET"])
def get_study():
    study = list(db.study_material.find({}, {"_id": 0}))
    return jsonify(study)