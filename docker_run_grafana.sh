

name=tutorial_hub_grafana

echo Tutorial Hub Grafana: Stopping
docker stop $name

echo Tutorial Hub Grafana: Removing
docker rm $name

docker run -d --name=$name -p 3000:3000 grafana/grafana