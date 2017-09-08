import sys
import time
import hashlib
import requests
import grequests

_version = sys.version_info
 is_python3 = (_version[0] == 3)
 
 orderno = "ZF2017941249NePjWY"
 secret = "6040074d0cde4b3daba76213dd665834"
  
 timestamp = str(int(time.time()))                # 计算时间戳
 string = ""
 string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp
  
 if is_python3:
      string = string.encode()
     
 md5_string = hashlib.md5(string).hexdigest()                 # 计算sign
 sign = md5_string.upper()                              # 转换成大写
 print(sign)
 auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp
  
 print(auth)
 proxy = {"http": "http://10.60.10.71:7789", "https": "https://10.60.10.71:7789"}
 headers = {"Proxy-Authorization": auth}
 r = requests.get("https://www.baidu.com", headers=headers, proxies=proxy, verify=False)
 print(r.status_code)
