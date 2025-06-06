# family-bank-2

Building on app family-bank.

## Running the backend app

```bash
make run-server
```

## Running the streamlit app

```bash
make run-client
```

## Running both the backend and the streamlit app

```bash
make run-all
```

## Stopping both the backend and the streamlit app

```bash
make stop-all
```

## Goals with this project

- [x] Add a new endpoint for creating a transaction
- [x] Add a new endpoint for getting transactions
- [x] Add a new endpoint for getting accounts
- [x] Add a new endpoint for getting parents

## Todos

- [x] Move models to models.py
- [x] Add a new endpoint for getting all transactions
- [x] Look at json in the other project to see how to store transactions
- [x]   Read all transactions from db file
- [x] Fix get transactions endpoint
- [x] Add a new endpoint for creation of a transaction
- [x]   Store transactions to db file
- [ ]   do input validation
- [ ]   add error handling
- [ ] Create a transaction model
- [x] Get streamlit to use the backend instead of the local file

## Testing the app

```bash
# using httpie
http POST http://localhost:8000/transactions/2 amount=10
```

```bash
# using curl
curl -X POST -H "Content-Type: application/json" -d '{"amount": 10}' http://localhost:8000/transactions/2
```

```bash
# 
curl -X POST http://localhost:8000/save
```

```bash
curl -X GET -v http://localhost:8000/parents
```

```bash
# using python
poetry run python scripts/test_client.py
```
