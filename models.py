from pydantic import BaseModel, Field
from typing import List
from src.auth import hash_password, verify_password

class ParentCreate(BaseModel):
    """
    Model for creating a new parent.
    This includes the plain password which will be hashed before storage.
    """
    name: str
    password: str

class Parent(BaseModel):
    """
    Model for a parent in the system.
    The password is stored as a hash.
    """
    id: int
    name: str
    password_hash: str = Field(..., alias="password", dump_alias="password")

    def verify_password(self, password: str) -> bool:
        """
        Verify if the provided password matches the stored hash.
        """
        return verify_password(password, self.password_hash)

    @classmethod
    def create(cls, id: int, name: str, password: str) -> "Parent":
        """
        Create a new Parent instance with a hashed password.
        """
        return cls(
            id=id,
            name=name,
            password_hash=hash_password(password)
        )

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
