from pydantic import BaseModel
from typing import List

class Parent(BaseModel):
    id: int
    name: str

class Transaction(BaseModel):
    id: int
    amount: float
    child_account_id: int
    description: str

class TransactionCreate(BaseModel):
    amount: float
    child_account_id: int
    description: str

class ChildAccount(BaseModel):
    id: int
    owner: str
    history: List[Transaction] = []
