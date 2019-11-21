# -*- coding:utf-8 -*-

import requests
import mytoken

#登录后在个人中心获取
spiderId = "8ea1baef1c3037ed83182b4a0d7ba5c9"
secret = "0f5c79113f2f43fbad613382daac8297"

"""
申请拨号服务器
"""
def applyChannels():
    params = {"count": 20}

    timestamp = mytoken.getTime();
    token = mytoken.gen_token(spiderId, secret, params, timestamp)
    apply_headers = mytoken.genHeaders(token, spiderId, timestamp);

    try:
        r = requests.get("http://api.xdaili.cn/xdaili-api/spider/applyChannels", headers=apply_headers, json=params, timeout=120)
    except Exception as err_info:
        r = None
        print(err_info)

    if r is not None:
        print(r.status_code)
        if r.status_code == 200:
            print(r.content)
            print(r.json())
            result = r.json()
            if result["ERRORCODE"] == "0" and result["RESULT"]:
                for one in result["RESULT"]:
                    print(one)
                    print(one["proxyId"])
                    print(one["orderno"])
                    getDynamicIP(one["orderno"], one["proxyId"])
"""
动态拨号
"""
def getDynamicIP(orderno, proxyId):
    url = "http://api.xdaili.cn/xdaili-api/privateProxy/getDynamicIP" + "/" + orderno + "/" + proxyId
    try:
        r = requests.get(url, timeout=120)
    except Exception as err_info:
        r = None
        print(err_info)

    if r is not None:
        print(r.status_code)
        if r.status_code == 200:
            print(r.content)
            print(r.json())
            result = r.json()
            if result["ERRORCODE"] == "0" and result["RESULT"]:
                print(result["RESULT"]["wanIp"])
                print(result["RESULT"]["proxyport"])


applyChannels()
