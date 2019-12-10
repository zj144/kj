'''
需求：
1. 请求IHRM项目的登录接口，请求数据（ {"mobile":"13800000002", "password":"123456"} ）
2. 登录接口URL：http://182.92.81.159/api/sys/login
'''
import requests
url = 'http://182.92.81.159/api/sys/login'
json = {"mobile":"13800000002", "password":"123456"}
r = requests.post(url,json= json)

print(r.json())