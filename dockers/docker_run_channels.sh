
docker stop burning_man
docker rm burning_man
docker run -d \
    -p 8001:8001 \
    --name university_channels university_django \
    daphne -p 8001 -b 0.0.0.0 project.asgi:application