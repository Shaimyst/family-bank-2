import streamlit as st
import json
import hashlib
import requests

st.title("Sadler Family Bank")

base_url = "http://localhost:8000"  # TODO: Make this configurable?
parents_response = requests.get(f"{base_url}/parents")
parents_data = parents_response.json()
st.json(parents_data)

child_accounts_response = requests.get(f"{base_url}/child-accounts")
child_accounts_data = child_accounts_response.json()
st.json(child_accounts_data)

transactions_response = requests.get(f"{base_url}/transactions")
transactions_data = transactions_response.json()
st.json(transactions_data)

# TODO:
# - [X] Get streamlit to use the backend instead of the local file
# - [X] Update references to parents to use the backend
# - [X] Update references to child accounts to use the backend
# - [ ] Update references to transactions to use the backend
# - [ ] Update references to password hashes to use the backend


# # Constants
# PASSWORD_HASHES: dict[str, str] = {
#     # TODO: Get these from the backend
#     "Harry": "7e0464e879d5cb4cd54715be3d7124718b615befd980aa220290ddea72788bd6",
#     "Jessica": "baa64f239eb1af2d110f6c21481a025845c810ae299d92dc9ae7dfbedda0fe8b"
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

# # # Load transactions from save file
# # with open("db.json", "r") as f:
# #     transactions: list[Transaction] = []
# #     try:
# #         contents = json.load(f)
# #         for transaction in contents["transactions"]:
# #             transactions.append(
# #                 Transaction(
# #                     transaction["child"], 
# #                     transaction["amount"], 
# #                     transaction["description"], 
# #                     transaction["parent"]
# #                 )
# #             )
# #     except Exception as e:
# #         print("No transactions found, will start with empty accounts")
# #     for transaction in transactions:
# #         if transaction.child == child_accounts_data[0]["owner"]:
# #             child_accounts_data[0].commit_transaction(transaction)
# #         elif transaction.child == child_accounts_data[1]["owner"]:
# #             child_accounts_data[1].commit_transaction(transaction)
# #         else:
# #             st.error("Invalid child name")


# # Transaction form (collects transaction inputs from user)
# st.header("Transaction")
# child_name = st.selectbox("Child: ", [child["owner"] for child in child_accounts_data])

# transaction_amount = st.number_input("Amount: ", step=1.0)
# transaction_description = st.text_input("Description: ")

# parent_names = [parent["name"] for parent in parents_data]
# parent_name = st.selectbox("Parent: ", parent_names)

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
#         success: bool = child_accounts_data[0].commit_transaction(
#             Transaction(child_accounts_data[0]["owner"], transaction_amount, transaction_description, parent_name)
#         )
#         if success: 
#                 st.success("Transaction successful")
#         else:
#             st.error("Transaction failed to commit, account would be overdrawn")
#         # Save transactions to save file
#         with open("db.json", "w") as f:
#             all_transactions: list[Transaction] = []
#             all_transactions.extend([t.to_dict() for t in child_accounts_data[0].transaction_history])
#             all_transactions.extend([t.to_dict() for t in child_accounts_data[1].transaction_history])
#             json.dump({"transactions": all_transactions}, f, indent=2)

# # Display balances
# st.write(f"{child_accounts_data[0]['owner']}'s balance: ", child_accounts_data[0].get_balance())
# st.write(f"{child_accounts_data[1]['owner']}'s balance: ", child_accounts_data[1].get_balance())
