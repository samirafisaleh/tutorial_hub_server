

source ../.env

docker stop $CONTAINER_NAME_REDIS
docker rm $CONTAINER_NAME_REDIS
docker run -d \
            --read-only \
            --network=$SERVER_NETWORK \
            --name $CONTAINER_NAME_REDIS $IMAGE_NAME_REDIS \
            redis-server --bind 0.0.0.0 --port $NETWORK_PORT_REDIS