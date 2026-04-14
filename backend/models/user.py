from config.db import get_db

def get_users_collection():
    return get_db()["users"]

def create_user(user):
    return get_users_collection().insert_one(user)

def find_user(username):
    return get_users_collection().find_one({"username": username})