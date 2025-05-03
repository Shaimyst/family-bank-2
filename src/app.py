from fastapi import FastAPI
import json
from models import Transaction, Parent, ChildAccount, TransactionCreate

# TODO: this file should only communicate to db.py

app = FastAPI(
    docs_url="/docs",
    title="Family Bank 2",
    version="0.1.0",
)

SAVE_FILE: str = "db.json"

@app.get("/parents")
async def get_parents() -> list[Parent]:
    try:
        with open(SAVE_FILE, "r") as f:
            database: dict = json.load(f)
            db_parents: list[dict] = database["parents"]
            parents = []
            for p in db_parents:
                parents.append(Parent(**p))
            return parents
    except FileNotFoundError:
        return []

@app.get("/child-accounts")
async def get_child_accounts() -> list[ChildAccount]:
    try:
        with open(SAVE_FILE, "r") as f:
            database: dict = json.load(f)
            db_child_accounts: list[dict] = database["child_accounts"]
            child_accounts = []
            for c in db_child_accounts:
                child_accounts.append(ChildAccount(**c))
            return child_accounts
    except FileNotFoundError:
        return []

@app.get("/transactions")
async def get_transactions() -> list[Transaction]:
    try:
        with open(SAVE_FILE, "r") as f:
            database: dict = json.load(f)
            db_transactions: list[dict] = database["transactions"]
            transactions=[]
            for t in db_transactions:
                transactions.append(Transaction(**t))
            return transactions
    except FileNotFoundError:
        return []

@app.post("/transactions")
async def create_transaction(transaction_create: TransactionCreate) -> Transaction:
    try:
        with open(SAVE_FILE, "r") as f:
            database = json.load(f)
    except FileNotFoundError:
        database = {"transactions": [], "parents": [], "child_accounts": []}

    transaction_dict = transaction_create.model_dump()
    transaction_dict["id"] = len(database.get("transactions", [])) + 1

    database["transactions"].append(transaction_dict)
    
    with open(SAVE_FILE, "w") as f:
        json.dump(database, f, indent=2)
    
    return Transaction(**transaction_dict)
