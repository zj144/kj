'''
查看响应结果reponse.text
requests实现GET请求
查看响应状态码reponse.status_code
'''
# 1.导包
import requests
r = requests.get('http://www.baidu.com')

print('查看响应状态码',r.status_code)
print('*'*20,'华丽分割'*20)
print(r.text)
