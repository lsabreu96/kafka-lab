FROM python:3.13.0-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY src/message_consumer.py message_consumer.py

CMD ["python", "message_consumer.py"]
