import json
from pathlib import Path
from datetime import datetime

USERS_FILE = Path("app/storage/users.json")
POSTS_FILE = Path("app/storage/posts.json")

users = []
posts = []

def _serialize(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # конвертация datetime -> строка
    raise TypeError(f"Type {type(obj)} not serializable")

def load_data():
    global users, posts
    if USERS_FILE.exists():
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = []

    if POSTS_FILE.exists():
        with open(POSTS_FILE, "r", encoding="utf-8") as f:
            try:
                posts = json.load(f)
            except json.JSONDecodeError:
                posts = []

def save_data():

    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2, default=_serialize)

    with open(POSTS_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2, default=_serialize)
