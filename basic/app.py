from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template("index.html", number1=12, number2=34)


@app.route('/error')
def hello_boo():
    return render_template("error.html", code=404)


if __name__ == '__main__':
    app.run()