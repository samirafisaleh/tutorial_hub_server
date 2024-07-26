
major=0
minor=0
patch=1
reltype=dev 

build_name=tutorial_hub_prometheus:$reltype-$major.$minor.$patch 
echo "Build: $build_name"

echo "Build: Removing $build_name"
docker rmi $build_name

echo "Build: Creating $build_name"
docker build -t $build_name -f  Dockerfile_prometheus.Dockerfile .