
run-server:
	poetry run uvicorn src.app:app --reload --log-level debug

run-client:
	poetry run streamlit run src/client.py
