import sys
import time
import hashlib
import requests
import grequests


_version = sys.version_info

is_python3 = (_version[0] == 3)

orderno = "ZF2017985116rTEkIY"
secret = "bbaee8bad1d44cee9621474cf8c0de96"

ip = "10.60.20.115"
port = "7789"

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
r = requests.get("https://www.baidu.com", headers=headers, proxies=proxy, verify=False)
print(r.status_code)
print(r.content)
print(r.text)

while True:
    urls = ["http://nba.hupu.com"] * 10
    # urls = ["https://www.baidu.com"] * 10
    print(urls)
    start = time.time()
    r = (grequests.get(u, proxies=proxy, headers=headers, timeout=30, verify=False, allow_redirects=False) for u in urls)
    r_list = grequests.map(r)
    stop = time.time()
    print(r_list)
    print(stop - start)
