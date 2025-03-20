from pydantic import BaseModel
from typing import Optional, List
class Parent(BaseModel):
    id: int
    name: str

class Transaction(BaseModel):
    id: int
    amount: float
    child_account_id: int = None
    description: Optional[str] = None

class TransactionCreate(BaseModel):
    amount: float
    child_account_id: Optional[int] = None
    description: Optional[str] = None

class ChildAccount(BaseModel):
    id: int
    owner: str
    history: List[Transaction] = []
