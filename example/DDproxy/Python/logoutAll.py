# -*- coding:utf-8 -*-
import requests
import mytoken

# 登录后在个人中心获取
spiderId = "8ea1baef1c3047ed83182b4a0dsba5c9"
secret = "0f5c79113f2f43fbae613d82daac8297"

timestamp = mytoken.getTime();
token = mytoken.gen_token(spiderId, secret, "", timestamp)
logoutall_headers = mytoken.genHeaders(token, spiderId, timestamp);

try:
    r = requests.get("http://api.xdaili.cn/xdaili-api/spider/logOutAll",
            headers=logoutall_headers, timeout=120)
except Exception as err_info:
    r = None
    print(err_info)

if r is not None:
    print(r.status_code)
    if r.status_code == 200:
        print(r.content)
        print(r.json())
