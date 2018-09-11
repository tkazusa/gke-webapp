# -*- encoding: UTF-8 -*-
import os
import sys
import json
import pandas as pd
import pytest

sys.path.append("../../../backend/src")


from backend import People, post

'''
requests_data = {"row1":
                 {
                     "Pclass": "Test",
                     "Name": "John, Mr. Manjiro",
                     "Ticket": "c123",
                     "Sex": "Male",
                     "Age": 23,
                     "SibSp": 2,
                     "Parch": 0,
                     "Cabin": "Test",
                     "Embarcked": "Test"}}
data = json.dumps(requests_data)
data = pd.read_json(data, orient='index')
'''


def test_new_people():
    """Check the given data when People created"""
    people = People(data)
    assert people.data == data


def test_status_predict():
    """Check the predict method"""
    people = People(data)
    status = people.status_prediction()
    assert status == 1 or status == 0
