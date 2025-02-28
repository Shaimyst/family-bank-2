# family-bank-2
Building on app family-bank.

## Running the app

```bash
poetry run uvicorn src.app:app --reload --log-level debug
```

## Goals with this project

- [x] Add a new endpoint for creating a transaction
- [x] Add a new endpoint for getting transactions
- [x] Add a new endpoint for getting accounts
- [x] Add a new endpoint for getting parents

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
