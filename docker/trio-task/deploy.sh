#!/bin/bash

MY_SQL_ROOT_PASSWORD=password

# remove running containers
docker rm -f $(docker ps -qa)

# create network
docker network create trio-task-network

# build flask and mysql image
docker build -t trio-task-mysql:5.7 db
docker build -t trio-task-app:latest flask-app

# run mysql container
docker run -d --name mysql \
    --network trio-task-network \
    -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD \
    -e MYSQL_DATABASE=flask.db \
    trio-task-mysql:5.7

# run flask container
docker run -d --name flask-app \
    --network trio-task-network \
    -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD \
    trio-task-app:latest

# nginx container
docker run -d --name nginx \
    -p 80:80 \
    --network trio-task-network \
    --mount type=bind,source=$(pwd)/nginx/nginx.conf,target=/etc/nginx/nginx.conf nginx:latest

# show running containers
docker ps -a