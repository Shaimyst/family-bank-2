import json

from models import Transaction, Parent, ChildAccount

# this is the database api for the backend

SAVE_FILE: str = "db.json"

def get_parents() -> list[Parent]:
    with open(SAVE_FILE, "r") as f:
        parents_data = json.load(f)["parents"]
        return [Parent(**parent) for parent in parents_data]

def get_child_accounts() -> list[ChildAccount]:
    with open(SAVE_FILE, "r") as f:
        child_accounts_data = json.load(f)["child_accounts"]
        return [ChildAccount(**child_account) for child_account in child_accounts_data]

def get_transactions() -> list[Transaction]:
    with open(SAVE_FILE, "r") as f:
        transactions_data = json.load(f)["transactions"]
        return [Transaction(**transaction) for transaction in transactions_data]

def create_transaction(transaction: Transaction) -> Transaction:
    with open(SAVE_FILE, "r") as f:
        db = json.load(f)
        # Find the next id
        next_id = 1
        if db["transactions"]:
            next_id = max(t.get("id", 0) for t in db["transactions"]) + 1
        
        # Add id to the transaction if it doesn't have one
        transaction_dict = transaction.model_dump()
        if "id" not in transaction_dict:
            transaction_dict["id"] = next_id
        
        db["transactions"].append(transaction_dict)
    
    with open(SAVE_FILE, "w") as f:
        json.dump(db, f, indent=2)
    
    return transaction
