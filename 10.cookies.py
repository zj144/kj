'''
响应对象常用方法
1.rp.cookies  #查看响应cookies
2.rp.content #以字节码形式解析数据

'''

# 将字节码写入图片
import requests

rp = requests.get('https://www.baidu.com')
print('输出cookies',rp.cookies)

print(rp.cookies(['BDDRZ']))
# 以字节码形式解析数据输出数据
ss = rp.content

rp = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1575713240129&di=c973786574b932276890f34c77e956aa&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20180801%2F980557bbfb424b83aa1bd47277504c55.jpeg')
rp2 = rp.content
with open('./skr.jpeg','wb') as f:
    f.write(rp2)