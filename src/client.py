import streamlit as st
import json
import hashlib
import requests
# TODO:
# - [ ] Get streamlit to use the backend instead of the local file
# - [ ] Update references to parents to use the backend
# - [ ] Update references to child accounts to use the backend

st.title("Sadler Family Bank")

parents = requests.get("http://localhost:8000/parents")
st.code(parents.json())

# # Constants
# PASSWORD_HASHES: dict[str, str] = {
#     "Dada": "7e0464e879d5cb4cd54715be3d7124718b615befd980aa220290ddea72788bd6",
#     "Mamma": "baa64f239eb1af2d110f6c21481a025845c810ae299d92dc9ae7dfbedda0fe8b"
# }

# # Application objects

# class Transaction:
#     def __init__(self, child: str, amount: float, description: str, parent: str):
#         self.child: str = child
#         self.amount: float = amount
#         self.description: str = description
#         self.parent: str = parent

#     def to_dict(self) -> dict:
#         return {
#             "child": self.child,
#             "amount": self.amount,
#             "description": self.description,
#             "parent": self.parent
#         }

# class ChildAccount:
#     def __init__(self, child: str):
#         self.child: str = child
#         self.transaction_history: list[Transaction] = []
        
#     def get_balance(self) -> float:
#         return sum(transaction.amount for transaction in self.transaction_history)

#     def commit_transaction(self, transaction: Transaction) -> bool:
#         success: bool
#         if self.get_balance() + transaction.amount < 0:
#             success = False
#         else:
#             self.transaction_history.append(transaction)
#             success = True
#         return success


# # Instantiate child accounts
# willow_account = ChildAccount("Willow")
# penny_account = ChildAccount("Penny")

# # Load transactions from save file
# with open("transactions.json", "r") as f:
#     transactions: list[Transaction] = []
#     try:
#         contents = json.load(f)
#         for transaction in contents["transactions"]:
#             transactions.append(
#                 Transaction(
#                     transaction["child"], 
#                     transaction["amount"], 
#                     transaction["description"], 
#                     transaction["parent"]
#                 )
#             )
#     except Exception as e:
#         print("No transactions found, will start with empty accounts")
#     for transaction in transactions:
#         if transaction.child == "Willow":
#             success: bool = willow_account.commit_transaction(transaction)
#             if not success:
#                 st.error("Transaction failed to load, insufficient balance")
#         elif transaction.child == "Penny":
#             success: bool = penny_account.commit_transaction(transaction)
#             if not success:
#                 st.error("Transaction failed to load, insufficient balance")
#         else:
#             st.error("Invalid child name")


# # Transaction form (collects transaction inputs from user)
# st.header("Transaction")
# child = st.selectbox("Child: ", ["Willow", "Penny"])
# transaction_amount = st.number_input("Amount: ", step=1.0)
# transaction_description = st.text_input("Description: ")
# parent_name = st.selectbox("Parent: ", ["Dada", "Mamma"])
# parent_password = st.text_input("Password: ", type="password")

# def hash_password(s: str) -> str:
#     return hashlib.sha256(s.encode()).hexdigest()

# def validate_inputs(
#     transaction_amount: float,
#     parent_name: str,
#     parent_password: str
# ) -> bool:
#     if transaction_amount == 0:
#         st.error("Transaction amount cannot be 0")
#         return False
#     if hash_password(parent_password) != PASSWORD_HASHES[parent_name]:
#         st.error("Invalid password")
#         return False
#     return True

# # Commit transaction if button is clicked
# if st.button("Commit transaction"):
#     if validate_inputs(transaction_amount, parent_name, parent_password):
#         # Try to commit transaction to child account object
#         if child == "Willow":
#             success: bool = willow_account.commit_transaction(
#                 Transaction(child, transaction_amount, transaction_description, parent_name)
#             )
#             if success: 
#                 st.success("Transaction successful")
#             else:
#                 st.error("Transaction failed to commit, account would be overdrawn")
#         else:
#             success: bool = penny_account.commit_transaction(
#                 Transaction(child, transaction_amount, transaction_description, parent_name)
#             )
#             if success: 
#                 st.success("Transaction successful")
#             else:
#                 st.error("Transaction failed to commit, account would be overdrawn")
#         # Save transactions to save file
#         with open("transactions.json", "w") as f:
#             all_transactions: list[Transaction] = []
#             all_transactions.extend([t.to_dict() for t in willow_account.transaction_history])
#             all_transactions.extend([t.to_dict() for t in penny_account.transaction_history])
#             json.dump({"transactions": all_transactions}, f, indent=2)

# # Display balances
# st.write("Willow's balance: ", willow_account.get_balance())
# st.write("Penny's balance: ", penny_account.get_balance())
