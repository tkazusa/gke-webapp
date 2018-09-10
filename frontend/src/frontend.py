#!/user/bin/env python

import requests
import json
from collections import namedtuple

from flask import Flask, request, render_template
app = Flask(__name__)


URL = "http://backend:8081"

data = {'name': 'hiraki',
        'age': 30}
headers = {'Content-Type': 'application/json'}


@app.route('/', methods=["GET"])
def render_input_form():
    return render_template('index.html')


@app.route('/', methods=["POST"])
def result():
    INPUT_DATA = {
        "Pclass": request.form["pclass"],
        "Name": request.form["name"],
        "Ticket": request.form["ticket"],
        "Sex": request.form["sex"],
        "Age": request.form["age"],
        "SibSp": request.form["Sibsp"],
        "Parch": request.form["parch"],
        "Cabin": request.form["cabin"],
        "Embarked": request.form["embarked"]}

    response = requests.post(URL, data=json.dumps(INPUT_DATA), headers=headers)
    return render_template('result.html', status=response.text)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)
