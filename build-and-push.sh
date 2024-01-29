#!/bin/bash

# Script pour construire et pousser une image Docker

if [ "$1" == "mysql" ]; then
    docker build -t $DOCKER_USERNAME/mysql:latest ./mysql
    docker push $DOCKER_USERNAME/mysql:latest
elif [ "$1" == "api" ]; then
    docker build -t $DOCKER_USERNAME/api:latest ./api
    docker push $DOCKER_USERNAME/api:latest
elif [ "$1" == "model" ]; then
    docker build -t $DOCKER_USERNAME/model:latest ./model
    docker push $DOCKER_USERNAME/model:latest
else
    echo "Usage: $0 [mysql|api|model]"
    exit 1
fi
