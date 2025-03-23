echo "Starting Docker compose..."
docker-compose up --build -d

sleep 5

docker ps -a

echo "Complete!"

