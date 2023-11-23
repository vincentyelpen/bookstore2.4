import requests
import json

url = "http://127.0.0.1:8000/add_book/"
data = {
    "author": "Cheng",
    "title": "Ceam the helloworld",
    "price": 10.99
}

response = requests.post(url, json=data)
print(response.json())
