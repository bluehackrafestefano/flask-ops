# flask-ops

- User data of the instance:
```bash
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
```

- Create app.py, error.html, index.html 
- 