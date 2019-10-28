import requests
import json
import time
url = 'https://ikea-snapup.woaap.com/snapup/submit'
data = {
    "city":"6",#城市编号
    "goods":"3,5,12"#商品编号
}
# 2中袋 3挂钟 5蒙娜丽莎 12地毯
headers = {"Accept": "application/json","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-cn","Connection": "keep-alive",
           "Content-Type": "application/json;charset=utf-8",
           "Cookie": "你的token"
time.sleep(5) #防止过早预约被识别为机器人
while True:
    r = requests.post(url=url,headers=headers,data=json.dumps(data))
    A = r.text.encode('utf-8').decode('unicode_escape')
    print(A)
    dataS = json.loads(r.text)
    errcode = dataS["errcode"]
    if errcode == "0":
        code = dataS["data"]["code"]
        print("预约成功,预约码:{}".format(code))
        break
    else:
        print("预约失败，重试中...")
    time.sleep(2)
