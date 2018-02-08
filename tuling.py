import requests
print("你好，我是图灵机器人")
while 1:
    s = input()
    resp = requests.post("http://www.tuling123.com/openapi/api", data={
        "key": "a3bd7519c8554650993e3e1d7d8a3d5f",
        "info": s,
        "userid": "123456"
    })
    resp = resp.json()
    print(resp['text'])