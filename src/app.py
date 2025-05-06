import json

from fastapi import FastAPI
import db
import models

# TODO: this file should only communicate to db.py

app = FastAPI(
    docs_url="/docs",
    title="Family Bank 2",
    version="0.1.0",
)

SAVE_FILE: str = "db.json"

@app.get("/parents")
async def get_parents() -> list[models.Parent]:
    return db.get_parents()

@app.get("/child-accounts")
async def get_child_accounts() -> list[models.ChildAccount]:
    return db.get_child_accounts()

@app.get("/transactions")
async def get_transactions() -> list[models.Transaction]:
    return db.get_transactions()

@app.post("/transactions")
async def create_transaction(transaction_create: models.TransactionCreate) -> models.Transaction:
    return db.create_transaction(transaction_create)
