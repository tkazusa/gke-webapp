# -*- encoding: UTF-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    name = "hello get"
    return name


@app.route('/', methods=['POST'])
def post():
    name = "hello post"
    return name

@app.route('/')
def good():
    name = "good"
    return name

if __name__ == "__main__":
    app.run(debug=True)

