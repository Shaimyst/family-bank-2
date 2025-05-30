import bcrypt

# The work factor determines how computationally intensive the hashing is
# Higher numbers are more secure but slower
# 12 is a good default that balances security and performance
WORK_FACTOR = 12

def hash_password(password: str) -> str:
    if not password:
        raise ValueError("Password cannot be empty")
    
    # Generate a salt with our work factor
    salt = bcrypt.gensalt(rounds=WORK_FACTOR)
    # Hash the password and convert the bytes to a string
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    if not plain_password or not hashed_password:
        raise ValueError("Both password and hash must be provided")
    
    try:
        return bcrypt.checkpw(
            plain_password.encode('utf-8'), 
            hashed_password.encode('utf-8')
        )
    except Exception as e:
        # Log the error in a real application
        print(f"Error verifying password: {e}")
        return False
