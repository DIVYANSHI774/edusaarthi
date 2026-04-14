from pymongo import MongoClient

MONGO_URI = "mongodb+srv://divyanshivats77_db_user:EduSaarthi123@cluster0.wvwidpa.mongodb.net/edusaarthi?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["edusaarthi"]

users = db["users"]
notices = db["notices"]
study = db["study_material"]
faq = db["faq"]
