#!/bin/bash
docker-compose down --volumes
IMAGE_NAME="phpdoc_web:latest"
docker rmi "$IMAGE_NAME"
IMAGE_NAME="phpdoc_ssh:latest"
docker rmi "$IMAGE_NAME"
echo "Cleanup complete."

