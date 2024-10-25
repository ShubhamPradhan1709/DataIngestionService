PYTHON = python3
APP_NAME = data-ingestion-service
IMAGE_NAME = $(APP_NAME):latest

environment:
	$(PYTHON) -m pip install -r requirements.txt

run:
	docker run -p 8000:8000 $(IMAGE_NAME)

package:
	docker build -t $(IMAGE_NAME) .

start:
	uvicorn app:app