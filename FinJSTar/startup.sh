#!/bin/bash

echo "Starting Docker Compose..."
docker-compose up --build -d

echo "Waiting for the container to start..."
sleep 5

echo "Checking running containers..."
docker ps -a

echo "Starting cron service in the container..."
docker exec working_man service cron restart

echo "Starting Flask application..."
docker exec working_man gosu webuser flask run --host=0.0.0.0 --port=5000 &

echo "Complete!"

