#!/bin/bash

# Остановка и удаление контейнеров
echo "Stopping and removing containers..."
docker-compose down --volumes

# Удаление Docker-образа
IMAGE_NAME="nodetar_web:latest"
echo "Removing Docker image: $IMAGE_NAME"
docker rmi "$IMAGE_NAME"

#IMAGE_NAME="phpdoc_ssh:latest"
#echo "Removing Docker image: $IMAGE_NAME"
#docker rmi "$IMAGE_NAME"

echo "Cleanup complete."

