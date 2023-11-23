import requests
import json

url = "http://127.0.0.1:8000/aggregate_delete/"

data = {
    'book_array': [
        {'title': 'a'},
        {'title': 'b'}
    ]
}

json_data = json.dumps(data)

response = requests.delete(url, data=json_data, headers={'Content-Type': 'application/json'})

print('DELETE')
print(response.status_code)
print(response.json())