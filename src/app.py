from fastapi import FastAPI, Response
import json
from models import Transaction, Parent, ChildAccount

app = FastAPI(
    docs_url="/docs",
    title="Family Bank 2",
    version="0.1.0",
)

SAVE_FILE: str = "db.json"

@app.get("/parents")
async def get_parents() -> list[Parent]:
    return [
        Parent(name="Harry"),
        Parent(name="Jessica"),
    ]

@app.get("/child-accounts")
async def get_child_accounts() -> list[ChildAccount]:
    return [
        ChildAccount(owner="Willow", account_id=1),
        ChildAccount(owner="Penny", account_id=2),
    ]

@app.get("/transactions")
async def get_transactions() -> list[Transaction]:
    try:
        with open(SAVE_FILE, "r") as f:
            database: dict = json.load(f)
            transactions: list[dict] = database["transactions"]
            return transactions
    except FileNotFoundError:
        return []

@app.post("/transactions/{account_id}")
async def create_transaction(account_id: int, transaction: Transaction):
    print("account_id", account_id)
    print("amount", transaction.amount)
    return {
        "message": f"Transaction created for account {account_id}",
        "amount": transaction.amount
    }

    # # Save transactions to save file
    # with open("db.json", "w") as f:
    #     all_transactions: list[Transaction] = []
    #     all_transactions.extend([t.to_dict() for t in willow_account.transaction_history])
    #     all_transactions.extend([t.to_dict() for t in penny_account.transaction_history])
    #     json.dump({"transactions": all_transactions}, f, indent=2)
