


# University Server

*** This project is currently on pause. Other projects have taken priority. Seek to return at a later time ***

## Introduction

This repository maintains the full backend implemenation of the University Server. It contains the source code, deployment strategies, as well as CI/CD integration. The server source uses Django as the web server of choice.


## Requirements

This project requires a minimal of software to fully implement, build, and deploy, thus keeping the necessary components lightweight in general.

### Python

- Python 3.9.1 or later
- Pip

### Dockers

- Docker CLI v25.0.3 or later

## Technical Description



### Web Service

### Logging

### Containerization

### In Memory Cache

## Scripts

EACH SCRIPT SHALL BE EXECUTED ON THE SAME LEVEL DIRECTORY.

| Script | Description |
| ------ | ----- |
| docker_build_pgadmin.sh | Build Postgres Admin web portal image |
| docker_build_postgres.sh | Build Postgres image |
| docker_build_redis.sh | Build Redis image |
| docker_build.sh | Build Django Server image |
| docker_compose_down.sh | Pull down Docker Compose |
| docker_compose_up.sh | Pull up Docker Compose |
| docker_pull_pgadmin.sh | |
| docker_pull_postgres.sh | |
| docker_run_pgadmin.sh | |
| docker_run_postgres.sh | |
| docker_run_redis.sh | |
| docker_run_wf_django | |
| jenkins_start.sh | |
| jenkins_stop.sh | |


## Todo Tasks

- Jenkins CI/CD integration
- GitHub remote publishing
- Vagrant integration
- Grafana/Prometheus integration
- AWS Cognito

## References