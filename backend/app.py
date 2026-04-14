from flask import Flask
from flask_cors import CORS
import os

from routes.auth import auth_routes
from routes.admin import admin_routes
from routes.faq import faq_routes
from routes.chat import chat_routes

app = Flask(__name__)

# 🔥 CORS FIX (IMPORTANT for frontend)
CORS(app, resources={r"/*": {"origins": "*"}})

# 🔐 SECRET KEY
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "edusaarthi_secret_key")

# 🔹 Blueprints
app.register_blueprint(auth_routes, url_prefix="/auth")
app.register_blueprint(admin_routes, url_prefix="/admin")
app.register_blueprint(faq_routes, url_prefix="/faq")
app.register_blueprint(chat_routes)

# 🔹 Home route
@app.route("/")
def home():
    return {"message": "EduSaarthi Running 🚀", "status": "success"}

# 🚀 LOCAL RUN ONLY (Render will ignore this)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)