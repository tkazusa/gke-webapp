#!/usr/bin/env python
from flask import Flask, jsonify, request
import pandas as pd

from preprocess import preprocess
from predict import Predictor

app = Flask(__name__)


class People:
    def __init__(self, INPUT_DATA):
        self.data = INPUT_DATA

    def status_prediction(self):
        PreprocessedData = preprocess(self.data)
        model = Predictor()
        status = model.predict(PreprocessedData)
        return status


@app.route('/', methods=['POST'])
def post():
    data = request.json
    INPUT_DATA = pd.read_json(data)
    people = People(INPUT_DATA)
    status = people.status_prediction()

    response = jsonify(status)
    response.status_code = 200
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
