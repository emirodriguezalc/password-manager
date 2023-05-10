from utils.hash_password import hash_password
import json

def authenticate(username, password, file):
    try:
        with open(file, "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}

    if username in users and users[username] == hash_password(password):
        return username
