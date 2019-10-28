import requests
import time
while True:
    url = 'https://ikea-snapup.woaap.com/snapup/getStock?city=1' #城市编号
    headers = {"Accept": "application/json","Accept-Encoding": "br, gzip, deflate",
               "Accept-Language": "zh-cn","Connection": "keep-alive","Content-Type": "application/json;charset=utf-8",
               "Cookie": "", #插入你的tk
               "Host": "ikea-snapup.woaap.com","Referer": "https://ikea-snapup.woaap.com/snapup/choose?type=3","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.8(0x17000820) NetType/WIFI Language/zh_CN","X-Requested-With": "XMLHttpRequest",}
    r = requests.get(url = url,headers=headers)
    print(r.text)
    time.sleep(1)
