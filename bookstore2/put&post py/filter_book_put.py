import requests
import json

# 设置 Django 视图的 URL
url = "http://127.0.0.1:8000/filter/"

# 构造 PUT 请求的数据
data_put = {
    "author": "f",
    "title": " ",
    "min_price": 10.0,
    "max_price": 50.0
}  # 替换为你想要的实际数据

# 发送 PUT 请求
response_put = requests.put(url, data=json.dumps(data_put), headers={"Content-Type": "application/json"})

# 打印响应内容
print("PUT ：")
print(response_put.status_code)
print(response_put.json())
