
name=tutorial_hub_nginx

echo "Tutorial Hub Nginx: Stopping"
docker stop $name

echo "Tutorial Hub Nginx: Removing"
docker rm $name

echo "Tutorial Hub Nginx: Starting"
docker run --rm -d  --name $name -p 80:80 nginx