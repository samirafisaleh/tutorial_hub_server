
source ../.env
docker build --tag $IMAGE_NAME_REDIS -f Dockerfile_Redis .
