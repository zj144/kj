import requests

r = requests.get('http://192.168.38.63:8000/api/departments')
# 以txt形式解析数据
print(r.text)

# 以json形式解析数据
print(r.json())




