
name=tutorial_hub_vault

echo Tutorial Hub Vault: Stopping
docker stop $name

echo Tutorial Hub Vault: Removing
docker rm $name

docker run --cap-add=IPC_LOCK -p 8200:8200 -d --name=$name hashicorp/vault