    import requests

    spiderId = "180284b3ccc04a7b8196b59d6488f6da"    # 登录后在个人信息页面

    """
    token通过token的计算方法生成，timestamp为生成token时所用的时间戳，在生成token的代码中可找到。
    """
    headers = {"spiderId": spiderId, "timestamp": timestamp, "token": token}
    """
    93d3ce48b30a11e6802371d9ec16a600为申请拨号服务器时返回的proxyId，
    DD201611258363Jp5KmR为申请拨号服务器时返回的对应orderno，
    后面的键值对为需要注销的其他机器的对应proxyId和orderno。
    """
    params = {
            "map": {
                    "93d3ce48b30a11e6802371d9ec16a600": "DD201611258363Jp5KmR",
                    "key1": value1,
                    "key2": value2,
                    "key3": value3,
                    ...
            }
    }
    r = requests.get("http://api.xdaili.cn/ipagent/spider/logOut", headers=headers, json=params)

    print(r.status_code)               # 查看状态码
    print(r.content)                   # 查看返回的数据
    print(type(r.content))             # 查看数据类型
    print(r.json())                    # 相当于json.loads(r.content)
    print(r.json()["RESULT"])          # 获取结果
