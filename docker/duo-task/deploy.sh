#!/bin/bash

# delete all running containers
docker rm -f $(docker ps -qa)

# create docker network
docker network create duo-task-network

# build flask image
docker build -t duo-task-flask-app .

# run flask app container
docker run -d --name flask-app \
    --network duo-task-network \
    duo-task-flask-app

# nginx container
docker run -d --name duo-task-nginx \
    -p 80:80 \
    --network duo-task-network \
    --mount type=bind,source=$(pwd)/nginx.conf,target=/etc/nginx/nginx.conf nginx
