from db import verify_parent_password

def test_login():
    # Test Harry's login
    harry_result = verify_parent_password("Harry", "password")
    print(f"Harry login test: {'✅ Success' if harry_result else '❌ Failed'}")
    
    # Test Jessica's login
    jessica_result = verify_parent_password("Jessica", "password")
    print(f"Jessica login test: {'✅ Success' if jessica_result else '❌ Failed'}")
    
    # Test incorrect password
    wrong_password = verify_parent_password("Harry", "wrongpassword")
    print(f"Wrong password test: {'✅ Success' if not wrong_password else '❌ Failed'} (should fail)")
    
    # Test non-existent user
    nonexistent = verify_parent_password("NonexistentUser", "password")
    print(f"Non-existent user test: {'✅ Success' if not nonexistent else '❌ Failed'} (should fail)")

if __name__ == "__main__":
    print("Testing login functionality...")
    test_login() 
