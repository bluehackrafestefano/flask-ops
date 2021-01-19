# flask-ops

#! /bin/bash
# update os
yum update -y
# set server hostname as jenkins-server
hostnamectl set-hostname flask-server
# install git
yum install git -y
# install python3
yum install python3 -y
# install pip
yum install python-pip -y
# install flask
pip install flask -y