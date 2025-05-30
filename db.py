import json

from models import Transaction, Parent, ChildAccount, ParentCreate

# this is the database api for the backend

SAVE_FILE: str = "db.json"

def get_parents() -> list[Parent]:
    with open(SAVE_FILE, "r") as f:
        parents_data = json.load(f)["parents"]
        return [Parent.model_validate(parent) for parent in parents_data]

def get_parent_by_name(name: str) -> Parent:
    with open(SAVE_FILE, "r") as f:
        parents_data = json.load(f)["parents"]
        return next((Parent.model_validate(parent) for parent in parents_data if parent["name"] == name), None)

def create_parent(parent_create: ParentCreate) -> Parent:
    """
    Create a new parent in the database.
    """
    try:
        # Read the current database state
        with open(SAVE_FILE, "r") as f:
            db = json.load(f)
        
        # Calculate next ID
        next_id = 1
        if db["parents"]:
            next_id = max(p.get("id", 0) for p in db["parents"]) + 1

        # Create new parent with hashed password
        new_parent = Parent.create(
            id=next_id,
            name=parent_create.name,
            password=parent_create.password
        )

        # Add to database
        db["parents"].append(new_parent.model_dump(by_alias=True))

        # Write back to file
        with open(SAVE_FILE, "w") as f:
            json.dump(db, f, indent=2)

        return new_parent
    except Exception as e:
        print(f"Error creating parent: {e}")
        raise
    
def verify_parent_password(name: str, password: str) -> bool:
    """
    Verify if the provided password matches the stored hash.
    """
    parent = get_parent_by_name(name)
    if not parent:
        return False
    return parent.verify_password(password)
    

def get_child_accounts() -> list[ChildAccount]:
    with open(SAVE_FILE, "r") as f:
        child_accounts_data = json.load(f)["child_accounts"]
        return [ChildAccount(**child_account) for child_account in child_accounts_data]

def get_transactions() -> list[Transaction]:
    with open(SAVE_FILE, "r") as f:
        transactions_data = json.load(f)["transactions"]
        return [Transaction(**transaction) for transaction in transactions_data]

def create_transaction(transaction: Transaction) -> Transaction:
    with open(SAVE_FILE, "r") as f:
        db = json.load(f)
        # Find the next id
        next_id = 1
        if db["transactions"]:
            next_id = max(t.get("id", 0) for t in db["transactions"]) + 1
        
        # Add id to the transaction if it doesn't have one
        transaction_dict = transaction.model_dump()
        if "id" not in transaction_dict:
            transaction_dict["id"] = next_id
        
        db["transactions"].append(transaction_dict)
    
    with open(SAVE_FILE, "w") as f:
        json.dump(db, f, indent=2)
    
    return transaction
