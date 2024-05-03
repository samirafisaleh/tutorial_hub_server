docker stop americana_brand
docker rm americana_brand
docker network create university-network
docker run -d -p 8002:8002 \
        --network university-network \
        -e CELERY_BROKER_URL=redis://old_fashioned:6379 \
        -e CELERY_RESULT_BACKEND=redis://old_fashioned:6379 \
        --name university_celerybeat university_django \
        celery -A project beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler