docker stop the_grove
docker rm the_grove
docker network create university-network
docker run -d -p 8003:8003 \
            --network university-network \
            -e CELERY_BROKER_URL=redis://old_fashioned:6379 \
            -e CELERY_RESULT_BACKEND=redis://old_fashioned:6379 \
            --name university_celeryworker university_django \
            celery -A project worker --loglevel=info