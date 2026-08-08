.PHONY: requirements lint clean
requirements:
	pip install -r requirements.txt
lint:
	ruff check analysis
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
