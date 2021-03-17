import requests
import json

def cal(a):
    v2=a[0]
    v4=a[1]-1
    while True:
        v3=v2
        v6=0
        v7=10
        while True:
            v5=v3%10
            if v5==0:
                return v2
            v3=v3//10
            v6=max(v5,v6)
            v7=min(v5,v7)
            if v3<=0:
                break
        v2=v6*v7+v2
        v4=v4-1
        if v4<=0:
            break
    return(v2)

while True:
    url = "http://159.75.70.9:8081/pull?u=youruid"
    res=requests.get(url=url)
    d=json.loads(res.text)
    a=d["a"]
    t=d["t"]
    a=cal(a)
    url='http://159.75.70.9:8081/push?t=%s&a=%s'%(t,a)
    res=requests.get(url=url)
    print(res.text)