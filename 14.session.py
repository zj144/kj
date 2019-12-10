'''
session()类自动附加cookies

作用：
    1.自动记录服务器响应cookies信息
    2.同一个session 对象下一条请求时自动附加cookies

获取对象
'''
import requests

url_code = "http://localhost/index.php?m=Home&c=User&a=verify"
url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"
url_order = "http://localhost/Home/Order/order_list.html"
data = {"username": "13612345678", "password":"123456","verify_code":"8888"}

# 创建session对象
sesion = requests.Session()
# 获取cookies
sesion.get(url_code)
# 请求登录
sesion.post(url_login,data=data)
# 请求我的订单
rp = sesion.get(url_order)
print(rp.text)
