(
source venv/bin/activate
pytest test
black .
flake8 --exclude venv
mypy --ignore-missing-imports --exclude venv .
)