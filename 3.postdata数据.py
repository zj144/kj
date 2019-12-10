'''
新增资源
post方法结合data数据格式
requests.post(url,data,json)
参数：
    data;
    json:
'''

import requests
data = {'username':'13612345678','password':'123456','verify_code':'8888'}
requests.post('http://localhost/index.php?m=Home&c=User&a=do_login',data=data)