import requests
import json

parameters = {'name': 'tb3_0'}
res = requests.post('http://192.168.35.46:8081/regist', data=json.dumps(parameters))
j = json.loads(res.text)
print(j['message'])