
run-server:
	poetry run uvicorn src.app:app --reload --log-level debug

run-client:
	poetry run streamlit run src/client.py

run-all:
	poetry run uvicorn src.app:app --reload --log-level debug &
	poetry run streamlit run src/client.py

stop-all:
	kill $(pgrep -f "poetry run uvicorn src.app:app --reload --log-level debug")
	kill $(pgrep -f "poetry run streamlit run src/client.py")
