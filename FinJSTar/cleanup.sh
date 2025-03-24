#!/bin/bash

docker-compose down --volumes

IMAGE_NAME="finjstar_web:latest"

docker rmi "$IMAGE_NAME"


