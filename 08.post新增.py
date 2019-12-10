"""
    目标：以标准的RESTful风格项目，演示下json与data
    需求：
        学院资源新增
        url = "http://127.0.0.1:8000/api/departmnets/"
        data = 		{
			"data": [
					  {
						"dep_id": "T01",
						"dep_name": "Test学院",
						"master_name": "Test-Master",
						"slogan": "Here is Slogan"
					  }
					]
		}
"""
# 导包
import requests
import json
# 调用post方法
url = "http://192.168.38.63:8000/api/departments/"
data = {
			"data": [
					  {
						"dep_id": "T01609",
						"dep_name": "Test学院1201",
						"master_name": "Test-Master",
						"slogan": "Here is Slogan"
					  }
					]
		}
r = requests.post(url=url, data=json.dumps(data), headers={"Content-Type":"application/json"})
# 获取响应状态码
print(r.status_code)
# 以json形式获取响应结果
print(r.json())
