

source .env

docker stop $CONTAINER_NAME_GRAFANA
docker rm $CONTAINER_NAME_GRAFANA
docker run -d \
            --read-only \
            --network=$UNIVERSITY_NETWORK \
            -e "PGADMIN_DEFAULT_EMAIL=$1" \
            -e "PGADMIN_DEFAULT_PASSWORD=$2" \
            -p $HOST_PORT_GRAFANA:3000 \
            --name $CONTAINER_NAME_GRAFANA grafana-enterprise