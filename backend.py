# -*- encoding: UTF-8 -*-
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    name = "hello get"
    return name

@app.route('/', methods=['POST'])
def post():
    changed_name = request.json['name'] + str(request.json['age'])
    response = jsonify(changed_name)
    response.status_code = 200
    return response

if __name__ == "__main__":
    app.run(debug=True)

