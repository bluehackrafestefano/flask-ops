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

- Create app.py

```py
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
```

- Create index.html

```html
<!DOCTYPE html>
<head></head>
<body>

    <h1>

        Hello World

    </h1>

</body>
```

- Create error.html

```html
<!DOCTYPE html>
<body></body>
<h1>
    This is error page!
</h1>
```

- Run your app:
```bash
python ./flask-ops/app.py
```

