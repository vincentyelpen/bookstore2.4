import requests
import json

# Replace with the actual ID of the book you want to update or delete
book_id = 6
url = f"http://127.0.0.1:8000/update_book/{book_id}/"

# Construct the data for the PUT request
data_put = {
    "author": "",
    "title": "helloworld",
    "price": '',
}  # Replace with the actual data you want

# Send the PUT request
response_put = requests.put(url, data=json.dumps(data_put), headers={"Content-Type": "application/json"})

# Print the response content
print("PUT response:")
print(response_put.status_code)
print(response_put.json())
