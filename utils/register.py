import json
from utils.hash_password import hash_password


def register(username, password, file):
    try:
        with open(file, "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}

    if username in users:
        return False
    else:
        users[username] = hash_password(password)
        with open(file, "w") as f:
            json.dump(users, f)
        return True
