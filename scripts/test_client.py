import requests

# response = requests.get("http://localhost:8000/transactions")
# print(response.json())

response = requests.post("http://localhost:8000/transactions/1", json={"amount": 100})
print(f"Status code: {response.status_code}")
print("Response:")
print(response.json())
