import requests
import time
while True:
    url = 'https://ikea-snapup.woaap.com/snapup/getStock?city=1' #城市编号
    headers = {"Accept": "application/json","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-cn","Connection": "keep-alive","Content-Type": "application/json;charset=utf-8","Cookie": "XSRF-TOKEN=eyJpdiI6Ik54MU82VXZid0YreDBMWDdTQWNEdVE9PSIsInZhbHVlIjoidmE5UGhMNUM5NHliRVhwWHpOY3pYVXdRa05Gb0lVUFR6ZytMckJYcWdIajRTMDhwT2Jqc0lzN3RpSVR2M245SCIsIm1hYyI6ImMxN2ZkZDQ5OWRhZDA0MmY0MDZhMGE4NGFlODRjZmI2ZDZhZDBlMTc2NGQ2ZTRkMjdjMjNmNDllM2YwOWQ3MzYifQ%3D%3D; ikeamarkerad_session=eyJpdiI6IldkeW1ZR2ZSMG5QMGhDSVRic1dDS0E9PSIsInZhbHVlIjoiMWZTYlwvU1dYU1hjdDJ1MkdwRGNrOVN1N2RFT1JUOTJVbUtqYmxWOU5hZHQwWUJ2b2N2QUhaMFNhelJBbFVZNXEiLCJtYWMiOiI4NWIxOWI2NzBiZmQxNjM4YjA2ZmM5ZGIzYjg0NDE3ZDlhYmYwOWE0N2JhNGQ4YTBhMTU2ZmZlY2JjODE4YmZlIn0%3D; Hm_lpvt_963279c4aaa8536c4b0047aabf7790ee=1572247296; Hm_lvt_963279c4aaa8536c4b0047aabf7790ee=1572247296","Host": "ikea-snapup.woaap.com","Referer": "https://ikea-snapup.woaap.com/snapup/choose?type=3","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.8(0x17000820) NetType/WIFI Language/zh_CN","X-Requested-With": "XMLHttpRequest",}
    r = requests.get(url = url,headers=headers)
    print(r.text)
    time.sleep(1)
