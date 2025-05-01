# this is the database api for the backend

import json
from typing import List
from models import Transaction, Parent, ChildAccount

def get_transactions() -> List[Transaction]:
    with open("db.json", "r") as f:
        transactions_data = json.load(f)["transactions"]
        return [Transaction(**transaction) for transaction in transactions_data]

def create_transaction(transaction: Transaction) -> Transaction:
    with open("db.json", "r") as f:
        db = json.load(f)
        db["transactions"].append(transaction.dict())
    
    with open("db.json", "w") as f:
        json.dump(db, f)
    
    return transaction

def get_parents() -> List[Parent]:
    with open("db.json", "r") as f:
        parents_data = json.load(f)["parents"]
        return [Parent(**parent) for parent in parents_data]

def get_child_accounts() -> List[ChildAccount]:
    with open("db.json", "r") as f:
        child_accounts_data = json.load(f)["child_accounts"]
        return [ChildAccount(**child_account) for child_account in child_accounts_data]
