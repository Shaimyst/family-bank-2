import json
import hashlib
import requests

import streamlit as st


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


st.title("Sadler Family Bank")

# TODO: this file should only communicate to app.py

base_url = "http://localhost:8000"  # TODO: Make this configurable?

# Fetch data from backend
parents_response = requests.get(f"{base_url}/parents")
if parents_response.status_code != 200:
    st.error(f"Failed to fetch parents: {parents_response.status_code} - {parents_response.text}")
    parents_data = []
else:
    parents_data = parents_response.json()

child_accounts_response = requests.get(f"{base_url}/child-accounts")
if child_accounts_response.status_code != 200:
    st.error(f"Failed to fetch child accounts: {child_accounts_response.status_code} - {child_accounts_response.text}")
    child_accounts_data = []
else:
    child_accounts_data = child_accounts_response.json()

transactions_response = requests.get(f"{base_url}/transactions")
if transactions_response.status_code != 200:
    st.error(f"Failed to fetch transactions: {transactions_response.status_code} - {transactions_response.text}")
    transactions_data = []
else:
    transactions_data = transactions_response.json()

# Display child account balances
st.header("Account Balances")
for account in child_accounts_data:
    balance = sum(t["amount"] for t in transactions_data if t["child_account_id"] == account["id"])
    st.metric(label=f"{account['owner']}'s Balance", value=f"${balance:.2f}")

# Transaction form
st.header("New Transaction")
with st.form("transaction_form", clear_on_submit=True):
    child_name = st.selectbox("Child: ", [child["owner"] for child in child_accounts_data])
    transaction_amount = st.number_input("Amount: ", step=1.0)
    transaction_description = st.text_input("Description: ")
    parent_name = st.selectbox("Parent: ", [parent["name"] for parent in parents_data])
    parent_password = st.text_input("Password: ", type="password")
    
    submitted = st.form_submit_button("Submit Transaction")
    if submitted:
        transaction_create = Transaction(
            amount=transaction_amount,
            child_account_id=next((acc for acc in child_accounts_data if acc["owner"] == child_name), None)["id"],
            description=transaction_description
        )
        
        try:
            response = requests.post(f"{base_url}/transactions", json=transaction_create.to_dict())
            if response.status_code == 200:
                st.success("Transaction submitted successfully")
                # Refresh the transactions data
                transactions_response = requests.get(f"{base_url}/transactions")
                if transactions_response.status_code == 200:
                    transactions_data = transactions_response.json()
            else:
                st.error(f"Failed to submit transaction: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Error submitting transaction: {str(e)}")

# tabs
tab1, tab2 = st.tabs(["Recent Transactions", "Transaction History"])

with tab1:
    # Display recent transactions
    st.header("Recent Transactions")
    for transaction in transactions_data:
        child_account = next((acc for acc in child_accounts_data if acc["id"] == transaction["child_account_id"]), None)
        if child_account:
            st.write(f"{child_account['owner']}: ${transaction['amount']:.2f} - {transaction['description']}")

with tab2:
    # Display transaction history for a child account
    st.header("Transaction History")
    child_name = st.selectbox("Child: ", [child["owner"] for child in child_accounts_data])
    child_account = next((acc for acc in child_accounts_data if acc["owner"] == child_name), None)
    if child_account:
        st.write(f"Transactions for {child_account['owner']}:")
        # Using the already fetched transactions data instead of making a new request
        child_transactions = [t for t in transactions_data if t["child_account_id"] == child_account["id"]]
        if child_transactions:
            for transaction in child_transactions:
                st.write(f"${transaction['amount']:.2f} - {transaction['description']}")
        else:
            st.write("No transactions found for this account.")


# TODO:
# - [X] Get streamlit to use the backend instead of the local file
# - [X] Update references to parents to use the backend
# - [X] Update references to child accounts to use the backend
# - [X] Update references to transactions to use the backend
# - [X] Submitting transactions should clear the form
# - [X] Fix parents and child accounts not being cleared when submitting a transaction
# - [X] View transaction history for a child account
# - [ ] Update references to password hashes to use the backend


# # Constants
# PASSWORD_HASHES: dict[str, str] = {
#     # TODO: Get these from the backend
#     "Harry": "7e0464e879d5cb4cd54715be3d7124718b615befd980aa220290ddea72788bd6",
#     "Jessica": "baa64f239eb1af2d110f6c21481a025845c810ae299d92dc9ae7dfbedda0fe8b"
# }
