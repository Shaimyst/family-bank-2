from fastapi import FastAPI
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

@app.post("/transactions")
async def create_transaction(transaction: Transaction):
    # Load existing transactions or create empty list
    try:
        with open(SAVE_FILE, "r") as f:
            database = json.load(f)
            all_transactions = database.get("transactions", [])
    except FileNotFoundError:
        all_transactions = []
    
    transaction_dict = transaction.model_dump()
    
    # Get child accounts to look up by name
    child_accounts = await get_child_accounts()
    account = next((acc for acc in child_accounts if acc.owner.lower() == transaction.child_name.lower()), None)
    
    if not account:
        return {"error": f"Child '{transaction.child_name}' not found. Available children: {', '.join(acc.owner for acc in child_accounts)}"}
    
    # Create consistent transaction record
    transaction_dict = {
        "amount": transaction.amount,
        "child_name": transaction.child_name,
        "account_id": account.account_id,
        "id": len(all_transactions) + 1,
        "description": transaction.description
    }
    
    all_transactions.append(transaction_dict)
    
    with open(SAVE_FILE, "w") as f:
        json.dump({"transactions": all_transactions}, f, indent=2)
    
    return {
        "message": f"Transaction created for {transaction.child_name} (Account #{account.account_id})",
        "amount": transaction.amount,
        "transaction_id": transaction_dict["id"]
    }
