'''
？后浏览器

GET传参(关键字 params 传参)

需求：
    url='http://www.baidu.com/?name="张"'

'''
# 导包
import requests
# 创建字典传参
data = {"name":"张三","age":"26"}
# get请求网址
r = requests.get('https://www.baidu.com',params=data)
# 输出结果转码
r.encoding = 'utf8'
# 输出响应状态码
print(r.status_code)

# 文本形式输出响应体
# print(r.text)

# 输出url
print(r.url)

