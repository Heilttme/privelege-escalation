#!/bin/bash

echo "Stopping and removing containers..."
docker-compose down --volumes

IMAGE_NAME="finjstar_web:latest"
echo "Removing Docker image: $IMAGE_NAME"
docker rmi "$IMAGE_NAME"

echo "Cleanup complete."

