FROM python:3.9-slim

WORKDIR /app

RUN mkdir -p /app/data && \
    mkdir -p /app/templates && \
    chmod -R 777 /app

COPY requirements.txt .
COPY templates/ /app/templates/
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
