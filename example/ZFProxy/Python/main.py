import sys
import time
import hashlib
import requests
# import grequests
from lxml import etree

_version = sys.version_info

is_python3 = (_version[0] == 3)

orderno = "ZF20179xxxxxxxxx"
secret = "3f9c2ecac7xxxxxxxxxxxxxxxx"

ip = "forward.xdaili.cn"
port = "80"

ip_port = ip + ":" + port

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
proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
headers = {"Proxy-Authorization": auth}
r = requests.get("http://www.baidu.com", headers=headers, proxies=proxy, verify=False,allow_redirects=False)
print(r.status_code)
print(r.content)
print(r.status_code)
if r.status_code == 302:
    loc = r.headers['Location']
    url_f = "https://www.tianyancha.com" + loc
    print(loc)
    r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    print(r.status_code)
    print(r.text)
