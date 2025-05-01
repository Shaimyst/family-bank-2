import streamlit as st
import json
import hashlib
import requests

st.title("Sadler Family Bank")

base_url = "http://localhost:8000"  # TODO: Make this configurable?

# Fetch data from backend
parents_response = requests.get(f"{base_url}/parents")
parents_data = parents_response.json()


child_accounts_response = requests.get(f"{base_url}/child-accounts")
child_accounts_data = child_accounts_response.json()

transactions_response = requests.get(f"{base_url}/transactions")
transactions_data = transactions_response.json()

# Display child account balances
st.header("Account Balances")
for account in child_accounts_data:
    balance = sum(t["amount"] for t in transactions_data if t["child_account_id"] == account["id"])
    st.metric(label=f"{account['owner']}'s Balance", value=f"${balance:.2f}")

# Transaction form
st.header("New Transaction")
with st.form("transaction_form"):
    child_name = st.selectbox("Child: ", [child["owner"] for child in child_accounts_data])
    transaction_amount = st.number_input("Amount: ", step=1.0)
    transaction_description = st.text_input("Description: ")
    parent_name = st.selectbox("Parent: ", [parent["name"] for parent in parents_data])
    parent_password = st.text_input("Password: ", type="password")
    
    submitted = st.form_submit_button("Submit Transaction")
    if submitted:
        # TODO: Add transaction submission logic
        st.info("Transaction submission will be implemented next")

# Display recent transactions
st.header("Recent Transactions")
for transaction in transactions_data:
    child_account = next((acc for acc in child_accounts_data if acc["id"] == transaction["child_account_id"]), None)
    if child_account:
        st.write(f"{child_account['owner']}: ${transaction['amount']:.2f} - {transaction['description']}")

# TODO:
# - [X] Get streamlit to use the backend instead of the local file
# - [X] Update references to parents to use the backend
# - [X] Update references to child accounts to use the backend
# - [X] Update references to transactions to use the backend
# - [ ] Update references to password hashes to use the backend


# # Constants
# PASSWORD_HASHES: dict[str, str] = {
#     # TODO: Get these from the backend
#     "Harry": "7e0464e879d5cb4cd54715be3d7124718b615befd980aa220290ddea72788bd6",
#     "Jessica": "baa64f239eb1af2d110f6c21481a025845c810ae299d92dc9ae7dfbedda0fe8b"
# }

class Parent:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name
        }

class Transaction:
    def __init__(self, amount: float, child_account_id: int, description: str):
        self.amount = amount
        self.child_account_id = child_account_id
        self.description = description

    def to_dict(self) -> dict:
        return {
            "amount": self.amount,
            "child_account_id": self.child_account_id,
            "description": self.description
        }

class ChildAccount:
    def __init__(self, id: int, owner: str, history: list[Transaction]):
        self.id = id
        self.owner = owner
        self.history = history

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "owner": self.owner,
            "history": [transaction.to_dict() for transaction in self.history]
        }
