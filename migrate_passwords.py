import json
from src.auth import hash_password

SAVE_FILE = "db.json"

def migrate_passwords():
    # Read the current database
    with open(SAVE_FILE, "r") as f:
        db = json.load(f)
    
    # Update each parent's password to be hashed
    for parent in db["parents"]:
        plain_password = parent["password"]
        parent["password"] = hash_password(plain_password)
    
    # Write the updated database back
    with open(SAVE_FILE, "w") as f:
        json.dump(db, f, indent=2)
    
    print("Successfully migrated passwords to hashed versions!")

if __name__ == "__main__":
    migrate_passwords() 
