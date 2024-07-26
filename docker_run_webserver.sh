

name=tutorial_hub_webserver

echo "Tutorial Hub Webserver: Stopping"
docker stop $name

echo "Tutorial Hub Webserver: Removing"
docker rm $name

echo "Tutorial Hub Webserver: Running"
docker run --rm -d  --name $name -p 5000:5000 tutorial_hub:dev-0.0.1 /bin/bash dev_run_server.sh
