# -*- encoding: UTF-8 -*-
import requests
import json

URL = "http://localhost:5000"

data = {'name': 'hiraki',
        'age': 30}
headers = {'Content-Type': 'application/json'}

if __name__ == "__main__":
    print(requests.post(URL, data=json.dumps(data), headers=headers).text)

