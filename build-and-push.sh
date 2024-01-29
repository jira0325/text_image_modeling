#!/bin/bash

# Script pour construire et pousser une image Docker

if [ "$1" == "mysql" ]; then
    docker build -t ${{ secrets.USER_DOCKERHUB }}/mysql:latest ./mysql
    docker push ${{ secrets.USER_DOCKERHUB }}/mysql:latest
elif [ "$1" == "api" ]; then
    docker build -t ${{ secrets.USER_DOCKERHUB }}/api:latest ./api
    docker push ${{ secrets.USER_DOCKERHUB }}/api:latest
elif [ "$1" == "model" ]; then
    docker build -t ${{ secrets.USER_DOCKERHUB }}/model:latest ./model
    docker push ${{ secrets.USER_DOCKERHUB }}/model:latest
else
    echo "Usage: $0 [mysql|api|model]"
    exit 1
fi
