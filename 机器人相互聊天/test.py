from time import sleep
import requests

topic = input("起始话题：")
n = 10
while n > 0:
    res = requests.post("http://www.tuling123.com/openapi/api", data={"key": "e9c66bc2a57346278ce9c55275609c7a", "info":topic})
    res.encoding = 'utf-8'
    res = res.json()
    sleep(1)
    print("图灵机器人：\t", res['text'])
    topic = res['text']
    res = requests.get("http://api.qingyunke.com/api.php", {"key": "free", "appid":0, "msg":topic})
    res.encoding = 'utf-8'
    res = res.json()
    sleep(1)
    print("青云客：\t", res['content'])
    topic = res['content']
    n -= 1

# 后续：QQ小冰，微软小冰，小i(xiaoi.com)