# -*- coding:utf-8 -*-
import requests
import mytoken

# 登录后在个人中心获取
spiderId = "8ea1baef1c3047ed83182b4a0d7ba5c9"
secret = "0f5c79113f2f43fbae613382daac8297"

params = {
        "map": {
                "433a83d2f96d11e9af127cd30abda612":"DD201911218432z9iG9r"
        }
}

#token通过token的计算方法生成，timestamp为生成token时所用的时间戳，在生成token的代码中可找到。
timestamp = mytoken.getTime();
token = mytoken.gen_token(spiderId, secret, params, timestamp)
headers = mytoken.genHeaders(token, spiderId, timestamp);
r = requests.get("http://api.xdaili.cn/xdaili-api/spider/logOut", headers=headers, json=params)

print(r.status_code)               # 查看状态码
print(r.content)                   # 查看返回的数据
print(type(r.content))             # 查看数据类型
print(r.json())                    # 相当于json.loads(r.content)
print(r.json()["RESULT"])          # 获取结果
