import requests
import json

while True:

    url = "http://159.75.70.9:8081/pull?u=000001129E0756BDF50DDA29DC4FFF17"

    res=requests.get(url=url)
    #print(res.text)

    d=json.loads(res.text)
    a=d["a"]
    t=d["t"]
    #print(a)
    
    a.sort()

    m=0
    n=0
    for i in range(0,7):
        n=a[i]
        pan=[m+n,m-n,m*n]
        m=pan[(i+1)%3]
    

    url='http://159.75.70.9:8081/push?t=%s&a=%s'%(t,-1*m)
    res=requests.get(url=url)
    print(res.text)