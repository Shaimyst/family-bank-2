from pydantic import BaseModel
from typing import Optional
from datetime import date

class Parent(BaseModel):
    name: str

class ChildAccount(BaseModel):
    owner: str

class Transaction(BaseModel):
    amount: float
    date: str
    account_id: int
    id: Optional[int] = None
