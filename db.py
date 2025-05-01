# this is the database api for the backend

import json

def get_transactions():
    with open("db.json", "r") as f:
        return json.load(f)["transactions"]

def create_transaction(transaction):
    with open("db.json", "r") as f:
        db = json.load(f)
        db["transactions"].append(transaction)
        with open("db.json", "w") as f:
            json.dump(db, f)

def get_parents():
    with open("db.json", "r") as f:
        return json.load(f)["parents"]

def get_child_accounts():
    with open("db.json", "r") as f:
        return json.load(f)["child_accounts"]
