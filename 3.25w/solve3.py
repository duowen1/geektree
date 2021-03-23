import base64
import requests
import json

string=base64.b64decode('dmFyIF8weGU5MzY9WydBNTQ3Mzc4OCddOyhmdW5jdGlvbihfMHg0OGU4NWMsXzB4ZTkzNmQ4KXt2YXIgXzB4MjNmYzVhPWZ1bmN0aW9uKF8weDI4NThkOSl7d2hpbGUoLS1fMHgyODU4ZDkpe18weDQ4ZTg1Y1sncHVzaCddKF8weDQ4ZTg1Y1snc2hpZnQnXSgpKTt9fTtfMHgyM2ZjNWEoKytfMHhlOTM2ZDgpO30oXzB4ZTkzNiwweDE5NikpO3ZhciBfMHgyM2ZjPWZ1bmN0aW9uKF8weDQ4ZTg1YyxfMHhlOTM2ZDgpe18weDQ4ZTg1Yz1fMHg0OGU4NWMtMHgwO3ZhciBfMHgyM2ZjNWE9XzB4ZTkzNltfMHg0OGU4NWNdO3JldHVybiBfMHgyM2ZjNWE7fTt3aW5kb3dbXzB4MjNmYygnMHgwJyldPWZ1bmN0aW9uKF8weDMzNTQzNyl7dmFyIF8weDFhYWMwMj0weDMwZDNmO2Zvcih2YXIgXzB4M2JlZDZhPTB4MzBkM2Y7XzB4M2JlZDZhPjB4MDtfMHgzYmVkNmEtLSl7dmFyIF8weDM3NTM0MD0weDA7Zm9yKHZhciBfMHgxZGRiNzc9MHgwO18weDFkZGI3NzxfMHgzYmVkNmE7XzB4MWRkYjc3Kyspe18weDM3NTM0MCs9XzB4MzM1NDM3WydhJ11bMHgwXTt9XzB4Mzc1MzQwJV8weDMzNTQzN1snYSddWzB4Ml09PV8weDMzNTQzN1snYSddWzB4MV0mJl8weDNiZWQ2YTxfMHgxYWFjMDImJihfMHgxYWFjMDI9XzB4M2JlZDZhKTt9cmV0dXJuIF8weDFhYWMwMjt9Ow==')
print(string)

while True:
    url = "http://159.75.70.9:8081/pull?u=000001129E0756BDF50DDA29DC4FFF17"
    res=requests.get(url=url)
    d=json.loads(res.text)
    a=d["a"]
    t=d["t"]

    # 计算最小i,使得i*a[0]%a[2]==a[1]
    for i in range(1,a[1]):
        m=i*a[0]
        if m%a[2]==a[1]:
            break

    url='http://159.75.70.9:8081/push?t=%s&a=%s'%(t,i)
    res=requests.get(url=url)
    print(res.text)