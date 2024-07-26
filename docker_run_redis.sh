
name=tutorial_hub_redis

echo Tutorial Hub Redis: Stopping
docker stop $name

echo Tutorial Hub Redis: Removing
docker rm $name

echo Tutorial Hub Redis: Starting
docker run --rm -d  --name $name -p 6379:6379 redis 