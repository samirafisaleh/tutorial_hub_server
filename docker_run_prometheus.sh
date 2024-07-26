

name=tutorial_hub_prometheus

echo Tutorial Hub Prometheus: Stopping
docker stop $name

echo Tutorial Hub Prometheus: Removing
docker rm $name


docker run -p 9090:9090 --name $name bitnami/prometheus:latest