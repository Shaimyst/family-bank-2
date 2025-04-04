from fastapi import FastAPI
import json
from models import Transaction, Parent, ChildAccount, TransactionCreate

app = FastAPI(
    docs_url="/docs",
    title="Family Bank 2",
    version="0.1.0",
)

SAVE_FILE: str = "db.json"

@app.get("/parents")
async def get_parents() -> list[Parent]:
    return [
        Parent(id=1, name="Harry"),
        Parent(id=2, name="Jessica"),
    ]

@app.get("/child-accounts")
async def get_child_accounts() -> list[ChildAccount]:
    return [
        ChildAccount(owner="Willow", id=1),
        ChildAccount(owner="Penny", id=2),
    ]

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
            all_transactions = database.get("transactions", [])
    except FileNotFoundError:
        all_transactions = []

    transaction_dict = transaction_create.model_dump()
    transaction_dict["id"] = len(all_transactions) + 1

    all_transactions.append(transaction_dict)
    
    with open(SAVE_FILE, "w") as f:
        json.dump({"transactions": all_transactions}, f, indent=2)
    
    return Transaction(**transaction_dict)
