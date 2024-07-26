
name=tutorial_hub_celery_worker

echo "Tutorial Hub Celery Worker: Stopping"
docker stop $name

echo "Tutorial Hub Celery Worker: Removing"
docker rm $name

echo "Tutorial Hub Celery Worker: Starting"
docker run --rm -d  --name $name tutorial_hub celery -A project worker -l INFO
