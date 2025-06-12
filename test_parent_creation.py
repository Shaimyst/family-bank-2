#!/usr/bin/env python3

from db import create_parent, get_parents
from models import ParentCreate
import json

def test_parent_creation():
    print("Testing parent creation...")
    
    # Create a test parent
    try:
        parent = create_parent(ParentCreate(name='TestParent', password='testpass'))
        print(f"Created parent: {parent}")
        
        # Read from db to verify
        with open('db.json', 'r') as f:
            data = json.load(f)
        print(f"Parents in db: {data['parents']}")
        
        # Try to get all parents
        all_parents = get_parents()
        print(f"All parents: {all_parents}")
        
        return True
    except Exception as e:
        print(f"Error creating parent: {e}")
        return False

if __name__ == "__main__":
    test_parent_creation() 
