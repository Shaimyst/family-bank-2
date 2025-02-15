from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/parents") # <-- these are called endpoint handlers
async def get_parents():
    parents = {
        1: {"name": "Harry"},
        2: {"name": "Jessica"},
    }
    return parents

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
async def create_transaction(account_id: int):
    print("account_id", account_id)
    return {"message": f"Transaction created for account {account_id}"}
