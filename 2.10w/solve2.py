import requests
import json

while True:
    url = "http://159.75.70.9:8081/pull?u=000001129E0756BDF50DDA29DC4FFF17"
    res=requests.get(url=url)
    d=json.loads(res.text)
    a0=d["a"][0]
    t=d["t"]
    a=a0**2+a0
    url='http://159.75.70.9:8081/push?t=%s&a=%s'%(t,a)
    res=requests.get(url=url)
    print(res.text)