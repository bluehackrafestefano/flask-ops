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

- import render_template to serve web pages and modify app.py 

```jinja
return render_template("index.html", number1=12, number2=34)
```

- add some conditionals, create conditional.html

- create sql folder, create app.py
```py
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the Planetary API.'), 200


@app.route('/not_found')
def not_found():
    return jsonify(message='That resource was not found'), 404


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not old enough."), 401
    else:
        return jsonify(message="Welcome " + name + ", you are old enough!")


@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not old enough."), 401
    else:
        return jsonify(message="Welcome " + name + ", you are old enough!")


if __name__ == '__main__':
    app.run()
```

- import sqlalchemy before
pip3 install flask_sqlalchemy