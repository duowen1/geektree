import requests
import json

while True:
    url = "http://159.75.70.9:8081/pull?u=000001129E0756BDF50DDA29DC4FFF17"
    res=requests.get(url=url)
    d=json.loads(res.text)
    a0=d["a"]
    t=d["t"]
    url='http://159.75.70.9:8081/push?t=%s&a=%s'%(t,a0[0])
    res=requests.get(url=url)
    print(res.text)