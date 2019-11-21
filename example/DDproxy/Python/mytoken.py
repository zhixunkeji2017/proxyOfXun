# -*- coding:utf-8 -*-
import hashlib
import time
import json

#生成token
def gen_token(spiderId, secret, p, timestamp):
    sha1 = hashlib.sha1()
    param = ""
    if p != "":
        items = p.items()
        for key, value in items:
            val = "";
            if isinstance(value, dict):
                val = json.dumps(value,separators=(',',':'))
            elif isinstance(value, int):
                val = str(value);
            else:
                val = value;
            param += key;
            param += val;
    sha1.update(param.encode("utf-8"))
    print(param)
    sign = sha1.hexdigest().upper();
    print(sign)
    md5 = hashlib.md5()
    signStr = str(timestamp) + secret + sign;
    md5.update(signStr.encode("utf-8"))
    token = md5.hexdigest();
    print(token)
    return token

#生成时间戳(秒级别)
def getTime():
    t = time.time()
    timestamp = int(t)
    return timestamp;

#生成请求头
def genHeaders(token, spiderId, timestamp):
    apply_headers = {"token": token, "spiderId": spiderId, "timestamp": str(timestamp)}
    return apply_headers;
