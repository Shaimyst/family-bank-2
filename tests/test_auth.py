import pytest
from src.auth import hash_password, verify_password

def test_hash_password_creates_hash():
    """
    Test that hash_password creates a hash different from the original password.
    Verifies that:
    - The hash is different from the original password
    - The hash is a string
    - The hash is in bcrypt format (starts with $2b$)
    """
    password = "test_password"
    hashed = hash_password(password)
    
    assert hashed != password
    assert isinstance(hashed, str)
    assert hashed.startswith("$2b$")

def test_verify_password_correct_password():
    """
    Test that verify_password returns True for correct passwords.
    Verifies that a password matches its own hash.
    """
    password = "test_password"
    hashed = hash_password(password)
    
    assert verify_password(password, hashed) is True

def test_verify_password_incorrect_password():
    """
    Test that verify_password returns False for incorrect passwords.
    Verifies that wrong passwords don't match the hash.
    """
    password = "test_password"
    hashed = hash_password(password)
    
    assert verify_password("wrong_password", hashed) is False

def test_hash_password_empty_password():
    """
    Test that hash_password raises ValueError for empty passwords.
    Verifies our input validation works.
    """
    with pytest.raises(ValueError):
        hash_password("")

def test_verify_password_empty_inputs():
    """
    Test that verify_password raises ValueError for empty inputs.
    Verifies our input validation works for both password and hash.
    """
    with pytest.raises(ValueError):
        verify_password("", "some_hash")
    
    with pytest.raises(ValueError):
        verify_password("some_password", "")

def test_different_passwords_different_hashes():
    """
    Test that different passwords produce different hashes.
    Verifies that our hashing is working correctly and not producing
    the same hash for different passwords.
    """
    password1 = "password1"
    password2 = "password2"
    
    hash1 = hash_password(password1)
    hash2 = hash_password(password2)
    
    assert hash1 != hash2
