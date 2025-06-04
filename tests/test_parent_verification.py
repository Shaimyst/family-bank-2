import pytest
from db import verify_parent_password

def test_parent_verification_success():
    """Test that parent verification works for valid parents with correct passwords."""
    assert verify_parent_password("Harry", "password") is True
    assert verify_parent_password("Jessica", "password") is True

def test_parent_verification_wrong_password():
    """Test that verification fails with incorrect passwords."""
    assert verify_parent_password("Harry", "wrongpassword") is False

def test_parent_verification_nonexistent_parent():
    """Test that verification fails for non-existent parents."""
    assert verify_parent_password("NonexistentUser", "password") is False

def test_parent_verification_empty_inputs():
    """Test that verification returns False for empty parent name, and raises ValueError for empty password."""
    assert verify_parent_password("", "password") is False
    
    with pytest.raises(ValueError, match="Both password and hash must be provided"):
        verify_parent_password("Harry", "")

if __name__ == "__main__":
    print("Testing login functionality...")
    test_parent_verification_success()
    test_parent_verification_wrong_password()
    test_parent_verification_nonexistent_parent()
    test_parent_verification_empty_inputs() 
