
name=tutorial_hub_flower

echo "Tutorial Hub Gunicorn: Stopping"
docker stop $name

echo "Tutorial Hub Gunicorn: Removing"
docker rm $name

echo "Tutorial Hub Gunicorn: Starting"
docker run --rm -d  --name $name -p 5555:5555 tutorial_hub /bin/bash run_flower.sh
