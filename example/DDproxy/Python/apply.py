   
    # -*- coding:utf-8 -*-

    import requests

    from mytoken import gen_token

    spiderId = "7aff9cc6932d495484e9be4cd20cc158" //登录后在个人中心获取
    secret = "915bd197de454c71a23b2589b4b6d6b5"   //登录后在个人中心获取

    """
    申请拨号服务器
    """
    p = {"count": 20}
    apply_headers = gen_token(spiderId, secret, p)

    try:
        r = requests.get("http://api.xdaili.cn/xdaili-api/spider/applyChannels",
                headers=apply_headers, json=p, timeout=120)
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
                    
    """
    动态拨号
    """
    dial_headers = gen_token(spiderId, secret)
    url = "http://api.xdaili.cn/xdaili-api/privateProxy/getDynamicIP" + \
            "/" + one["orderno"] + "/" + one["proxyId"]
    try:
        r = requests.get(url, headers=dial_headers, timeout=120)
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
                
                
                
