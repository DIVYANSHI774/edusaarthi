from config.db import db

def get_answer(message):
    message = message.lower().strip()

    # 🔍 FAQ
    for faq in db.faq.find():
        question = faq.get("question", "").lower()
        if message in question:
            return faq.get("answer")

    # 🔍 STUDY MATERIAL (FIXED NAME ✅)
    for item in db.study_material.find():
        title = item.get("title", "").lower()
        content = item.get("content", "").lower()

        if message in title or message in content:
            return item.get("content")

    # 🔍 NOTICES
    for notice in db.notices.find():
        title = notice.get("title", "").lower()
        content = notice.get("content", "").lower()

        if message in title or message in content:
            return notice.get("content")

    # 🤖 DEFAULT
    return "Sorry 😅, this question is outside your study material."