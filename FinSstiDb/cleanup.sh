#!/bin/bash

docker-compose down --volumes

IMAGE_NAME="finsstidb_flask:latest"
docker rmi "$IMAGE_NAME"

IMAGE_NAME="finsstidb_ssh:latest"
docker rmi "$IMAGE_NAME"

