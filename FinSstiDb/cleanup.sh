#!/bin/bash

echo "Stopping and removing containers..."
docker-compose down --volumes

IMAGE_NAME="finsstidb_flask:latest"
echo "Removing Docker image: $IMAGE_NAME"
docker rmi "$IMAGE_NAME"

IMAGE_NAME="finsstidb_ssh:latest"
echo "Removing Docker image: $IMAGE_NAME"
docker rmi "$IMAGE_NAME"

echo "Cleanup complete."

