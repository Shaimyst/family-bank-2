from fastapi import FastAPI, Response
import json
from pydantic import BaseModel

app = FastAPI(
    docs_url="/docs",
    title="Family Bank 2",
    version="0.1.0",
)

SAVE_FILE: str = "db.json"

class Parent(BaseModel):
    name: str

@app.get("/parents") # <-- these are called endpoint handlers
async def get_parents() -> list[Parent]:
    return [
        Parent(name="Harry"),
        Parent(name="Jessica"),
    ]

@app.get("/accounts")
async def get_accounts():
    accounts = {
        1: {"name": "Willow", "account_id": 1},
        2: {"name": "Penny", "account_id": 2},
    }
    return accounts

@app.get("/transactions")
async def get_transactions():
    transactions = {
        1: {"amount": 100, "date": "2024-01-01", "account_id": 1},
        2: {"amount": 200, "date": "2024-01-02", "account_id": 2},
    }
    return transactions

@app.post("/transactions/{account_id}")
async def create_transaction(account_id: int, transaction: dict):
    print("account_id", account_id)
    print("amount", transaction.get("amount"))
    return {
        "message": f"Transaction created for account {account_id}",
        "amount": transaction.get("amount")
    }

@app.post("/save")
async def save():
    with open("db.json", "w") as f:
        json.dump({"hi": "there"}, f, indent=2)
    return Response(status_code=200)


    # # Save transactions to save file
    # with open("db.json", "w") as f:
    #     all_transactions: list[Transaction] = []
    #     all_transactions.extend([t.to_dict() for t in willow_account.transaction_history])
    #     all_transactions.extend([t.to_dict() for t in penny_account.transaction_history])
    #     json.dump({"transactions": all_transactions}, f, indent=2)
