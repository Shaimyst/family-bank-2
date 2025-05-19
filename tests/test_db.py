import json
import os
import pytest
from pathlib import Path

from db import get_transactions, SAVE_FILE
from models import Transaction

@pytest.fixture
def test_db():
    """Fixture to create a temporary test database and clean it up after tests."""
    # Store original database if it exists
    original_db = None
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, 'r') as f:
            original_db = f.read()
    
    # Create empty test database
    test_data = {
        "parents": [],
        "child_accounts": [],
        "transactions": []
    }
    with open(SAVE_FILE, 'w') as f:
        json.dump(test_data, f)
    
    yield  # This is where the test runs
    
    # Cleanup: restore original database or remove test database
    if original_db:
        with open(SAVE_FILE, 'w') as f:
            f.write(original_db)
    else:
        os.remove(SAVE_FILE)

def test_get_transactions_empty(test_db):
    """Test that get_transactions returns an empty list when database is empty."""
    transactions = get_transactions()
    assert isinstance(transactions, list)
    assert len(transactions) == 0

def test_get_transactions_with_data(test_db):
    """Test that get_transactions correctly reads transactions from the database."""
    # Create test data
    test_transaction = {
        "id": 1,
        "amount": 10.00,
        "description": "Test transaction",
        "child_account_id": 1,
        "parent_id": 1,
        "timestamp": "2024-03-20T12:00:00"
    }
    
    # Write test data to database
    with open(SAVE_FILE, 'r') as f:
        db = json.load(f)
    db["transactions"].append(test_transaction)
    with open(SAVE_FILE, 'w') as f:
        json.dump(db, f)
    
    # Test the function
    transactions = get_transactions()
    assert isinstance(transactions, list)
    assert len(transactions) == 1
    assert isinstance(transactions[0], Transaction)
    assert transactions[0].id == test_transaction["id"]
    assert transactions[0].amount == test_transaction["amount"]
    assert transactions[0].description == test_transaction["description"]
