import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

# 使用方法
file_path = r'C:\Users\25852\Desktop\books_data.json'
encoding = detect_encoding(file_path)
print(f"The encoding of {file_path} is {encoding}")
