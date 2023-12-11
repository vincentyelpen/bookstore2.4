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
search_keywords = [
    'artificial intelligence', 'augmented reality development', 'quantum computing algorithms',
    'nanorobotics', 'cybersecurity solutions', 'biometric identification', 'IoT applications',
    'blockchain technology innovations', '5G network advancements', 'advanced robotics research',
    'autonomous vehicles technology', 'space exploration missions', 'biomedical nanotechnology',
    'cognitive computing systems', 'synthetic biology applications', 'neuroengineering breakthroughs',
    'wearable technology trends', 'smart cities infrastructure', 'genomic editing techniques',
    'quantum sensors development', 'machine learning in finance', 'robotic surgery advancements',
    'financial planning algorithms', 'green architecture innovations', 'sustainable fashion materials',
    'cognitive neuroscience studies', 'innovations in indie game development', 'medical anthropology research',
    'science communication strategies', 'educational technology tools', 'fashion illustration software',
    'urban exploration technology', 'happiness economics research', 'medieval history digitization',
    'human-computer interaction advancements', 'comparative religion studies with AI', 'adventure travel tech guides',
    'ecosystem ecology modeling', 'designer biography documentaries', 'cutting-edge futuristic technology',
    'innovations in alternative medicine', 'financial markets predictive analytics', 'sports psychology tools',
    'historical fashion digitization', 'advancements in cognitive psychology research',
    'ethical considerations in medical research', 'graphic design principles in UX/UI', 'biographical novels in AI era',
    'ancient myths reinterpretation with technology', 'human geography mapping technologies',
    'philosophy of science in the digital age', 'virtual reality gaming experiences', 'sustainable living technologies',
    'neuroethics in AI era', 'alternative education technology tools', 'crime scene investigation tech',
    'modern dance choreography with technology', 'data visualization tools for insights',
    'historical romance in virtual reality', 'modern philosophy in the age of AI', 'ethical hacking tools and techniques',
    'futuristic architecture design software', 'documentary filmmaking with VR', 'programming for kids platforms',
    'human-animal bond studies with technology', 'entrepreneurial finance in the digital economy',
    'urban sociology studies with data analytics', 'political satire in the age of social media',
    'archaeoastronomy with advanced telescopes', 'animal behavior studies with technology',
    'financial literacy apps and platforms', 'experimental psychology with virtual experiments',
    'fashion retail with augmented reality', 'quantum computing applications', 'medical mysteries solving with AI',
    'graphic design history interactive experiences', 'environmental activism leveraging technology',
    'social entrepreneurship in the digital era', 'ancient art history preservation with technology',
    'personal branding in the age of social media', 'mindful eating apps and tech innovations',
    'historical linguistics digitization', 'computer graphics in virtual environments',
    'biomedical engineering breakthroughs'
]

# 设置每页返回的图书数量和总共要获取的数据量
items_per_page = 40  # 每个关键词获取的图书数量
total_items = 1000  # 总共要获取的图书数量

# 存储结果的列表
all_books = {'books': []}

# 发送请求并获取数据
for keyword in search_keywords:
    # 请求参数
    params = {
        'q': keyword,
        'key': api_key,
        'startIndex': 0,
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

# 将结果保存到本地文件
output_file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'books_data.json')
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(all_books, output_file, ensure_ascii=False, indent=2)

print(f"Data saved to {output_file_path}")
