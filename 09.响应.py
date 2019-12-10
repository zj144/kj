'''
响应对象常用方法
1.rp.headers  #查看响应信息头（场景token）
2.rp.encoding
    案例：百度
    1.查看响应编码
    2.设置响应编码
'''
# 导包
import requests
# 调用get请求
rp = requests.get('http://www.baidu.com')
# 获取响应头
print('输出响应头',rp.headers)
# 获取响应编码
print('查看响应编码，',rp.encoding)
# 设置编码格式
rp.encoding = 'utf-8'
# 以text格式输出响应体
print(rp.text)