docker stop americana_brand
docker rm americana_brand
docker network create university-network
docker run -d -p 5001:5001 \
    --network university-network \
    -e CELERY_BROKER_URL=redis://old_fashioned:6379 \
    -e CELERY_RESULT_BACKEND=redis://old_fashioned:6379 \
    --name university_flower university_django \
    celery -A project flower --port=5001