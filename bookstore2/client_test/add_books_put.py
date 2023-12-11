import json
import requests

url = 'http://127.0.0.1:8000/add_books/'
headers = {'Content-Type': 'application/json'}

# 读取本地的 books_data.json 文件
file_path = 'C:\\Users\\25852\\Desktop\\books_data.json'  # 请根据实际路径调整
with open(file_path, 'r', encoding='utf-8') as file:
    books_data = json.load(file)

# 发送 POST 请求
response = requests.post(url, data=json.dumps(books_data), headers=headers)

# 打印响应结果
print(response.status_code)
try:
    print(response.json())
except json.decoder.JSONDecodeError:
    print(response.text)
