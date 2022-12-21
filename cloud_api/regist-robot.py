import sys
import requests
import json

name = sys.argv[1]
server = sys.argv[2]
parameters = {'name': name}
res = requests.post('http://{}/regist'.format(server), data=json.dumps(parameters))