

source ../.env

docker stop $CONTAINER_NAME_SERVER
docker rm $CONTAINER_NAME_SERVER
docker run -d -p $HOST_PORT_SERVER:8000 \
            --network=$SERVER_NETWORK \
            --volume logging_data_hub:/data_hub_server/logging \
            --name $CONTAINER_NAME_SERVER $IMAGE_NAME_SERVER \
            wf_run_django.sh 0.0.0.0:8000