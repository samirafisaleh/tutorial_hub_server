

name=tutorial_hub_gunicorn

echo "Tutorial Hub Gunicorn: Stopping"
docker stop $name

echo "Tutorial Hub Gunicorn: Removing"
docker rm $name

echo "Tutorial Hub Gunicorn: Running"
docker run --rm -d  --name $name -p 8001:8001 tutorial_hub /bin/bash run_wsgi.sh
