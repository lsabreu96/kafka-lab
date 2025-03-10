FROM python:3.13.0-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY src/message_generator.py message_generator.py

CMD ["python", "message_generator.py"]
