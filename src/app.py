import json

from fastapi import FastAPI, HTTPException
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

@app.post("/parents")
async def create_parent(parent_create: models.ParentCreate) -> models.Parent:
    if db.get_parent_by_name(parent_create.name):
        raise HTTPException(status_code=400, detail="Parent already exists")
    return db.create_parent(parent_create)

@app.post("/parents/verify")
async def verify_parent(name: str, password: str) -> dict:
    if db.verify_parent_password(name, password):
        return {"status": "success"}
    raise HTTPException(
        status_code=401,
        detail="Invalid password"
    )

@app.get("/child-accounts")
async def get_child_accounts() -> list[models.ChildAccount]:
    return db.get_child_accounts()

@app.get("/transactions")
async def get_transactions() -> list[models.Transaction]:
    return db.get_transactions()

@app.post("/transactions")
async def create_transaction(
    transaction_create: models.TransactionCreate,
    parent_name: str,
    parent_password: str,
) -> models.Transaction:
    if not db.verify_parent_password(parent_name, parent_password):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    return db.create_transaction(transaction_create)
