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
    
    # Get child accounts to verify the account id
    child_accounts = await get_child_accounts()
    account = next((acc for acc in child_accounts if acc.id == transaction.child_account_id), None)
    
    if not account and transaction.child_account_id is not None:
        return {"error": f"Child account with ID {transaction.child_account_id} not found. Available accounts: {', '.join(f'{acc.owner} (ID: {acc.id})' for acc in child_accounts)}"}
    
    # Create consistent transaction record
    transaction_dict = {
        "id": len(all_transactions) + 1,
        "amount": transaction.amount,
        "child_account_id": transaction.child_account_id,
        "description": transaction.description
    }
    
    all_transactions.append(transaction_dict)
    
    with open(SAVE_FILE, "w") as f:
        json.dump({"transactions": all_transactions}, f, indent=2)
    
    account_info = f"(Account #{transaction.child_account_id})" if transaction.child_account_id else "(No account specified)"
    owner_name = account.owner if account else "System"
    
    return {
        "message": f"Transaction created for {owner_name} {account_info}",
        "amount": transaction.amount,
        "transaction_id": transaction_dict["id"]
    }
