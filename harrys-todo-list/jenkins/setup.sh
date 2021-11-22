#!/bin/bash

sudo apt update
sudo apt install python3-venv python3-pip python3 -y

# create/activate virtual environment
python3 -m venv venv
source venv/bin/activate

# install pip requirements (from requirements.txt)
pip3 install -r requirements.txt