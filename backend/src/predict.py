import numpy as np
from sklearn.externals import joblib
from settings import MODEL_PATH


class Predictor(object):
    """prediction class"""

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, data):
        return self.model.predict(data)
