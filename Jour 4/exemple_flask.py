from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/toto")
def toto():
    return "<p>On peut faire une autre route</p>"