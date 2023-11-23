import requests
import json
import os
import time
import random

# 替换成你的 API 密钥
api_key = ''

# API 端点
url = 'https://www.googleapis.com/books/v1/volumes'

# 搜索关键词列表
search_keywords = ['python programming', 'machine learning', 'web development']

# 设置每页返回的图书数量和总共要获取的数据量，每页返回的量尽量不要改
items_per_page = 40
total_items = 200

# 存储结果的列表
all_books = {'books': []}

# 发送请求并获取数据
for keyword in search_keywords:
    # 请求参数
    params = {
        'q': keyword,
        'key': api_key,
        'startIndex': 0,  # 请根据实际情况调整
        'maxResults': items_per_page
    }

    # 发送 GET 请求
    response = requests.get(url, params=params)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析 JSON 数据
        data = response.json()

        # 获取图书信息
        books = data.get('items', [])
        for book in books:
            volume_info = book.get('volumeInfo', {})
            title = volume_info.get('title', 'N/A')
            authors = volume_info.get('authors', ['N/A'])
            price_info = volume_info.get('saleInfo', {}).get('retailPrice', {})
            price = format(price_info.get('amount', random.uniform(10, 100)) if price_info else random.uniform(10, 100), '.2f')

            authors_str = ', '.join(authors)

            # 存储图书信息
            book_info = {
                'authors': authors_str,
                'title': title,
                'price': price
            }
            all_books['books'].append(book_info)

            # 打印实时获取的信息
            print(f"Title: {title}\nAuthor(s): {authors_str}\nPrice: {price}\n---")

    else:
        print(f"Error {response.status_code} for request (Keyword: {keyword}): {response.text}")

    # 在每个请求之后添加随机的延迟（1到3秒之间）
    time.sleep(random.uniform(1, 3))

# 将结果保存到本地文件（改成你macbook的实际想存储的目录）
output_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'books_data.json')
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(all_books, output_file, ensure_ascii=False, indent=2)

print(f"Data saved to {output_file_path}")
