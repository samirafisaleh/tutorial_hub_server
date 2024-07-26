
name=tutorial_hub_celery_beat

echo "Tutorial Hub Celery Beat: Stopping"
docker stop $name

echo "Tutorial Hub Celery Beat: Removing"
docker rm $name

echo "Tutorial Hub Celery Beat: Starting"
docker run --rm -d  --name $name tutorial_hub celery -A project beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
