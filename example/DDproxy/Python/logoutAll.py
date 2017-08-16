    # -*- coding:utf-8 -*-

    import requests

    from mytoken import gen_token

    spiderId = "7aff9cc6932d495484e9be4cd20cc158" //登录后在个人中心获取
    secret = "915bd197de454c71a23b2589b4b6d6b5"   //登录后在个人中心获取

    logoutall_headers = gen_token(spiderId, secret)

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
                          
