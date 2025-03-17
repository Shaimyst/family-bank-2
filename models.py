from pydantic import BaseModel
from typing import Optional, List
class Parent(BaseModel):
    name: str

class Transaction(BaseModel):
    amount: float
    child_name: str
    account_id: Optional[int] = None
    id: Optional[int] = None
    description: Optional[str] = None

class ChildAccount(BaseModel):
    owner: str
    account_id: int
    account_history: List[Transaction] = []
