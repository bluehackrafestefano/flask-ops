from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/boo')
def hello_boo():
    return 'Boooo!'


if __name__ == '__main__':
    app.run()