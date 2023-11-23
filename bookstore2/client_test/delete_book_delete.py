import requests

# 设置请求的URL和要删除的书籍的ID
url = ("http://127.0.0.1:8000/delete_book/10")  # 将1替换为你想删除的书籍的ID

# 发送 DELETE 请求
response = requests.delete(url)

# 打印响应
print(response.json())
