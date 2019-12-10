'''
    目标：删除一个资源
    方法：delete
'''

import requests
url ="http://192.168.38.63:8000/api/departments/{T01609}"
ss = requests.delete(url)

print('删除结果为空：',ss.text)

