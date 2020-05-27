import hashlib
import requests
import json
import uuid


def md5_sign(data, api_key):
    """
    MD5签名
    :param data:
    :param api_key: MD5签名需要的字符串
    :return: 签名后的字符串sign
    """
    md5 = hashlib.md5()
    md5.update((data + api_key).encode(encoding='UTF-8'))
    return str(md5.hexdigest())


def update():
    url = "http://cantest5.mankebao.cn/open/api"

    method = "api.base.supplierUser.update"
    dataData = {"userCode": "32232", "userName": "d3af", "tUserId": "9404"}

    data = {"data": json.dumps(dataData, separators=(',', ':')), "method": method, "requestId": "str(uuid.uuid1())", "supplierCode": "300123", "timestamp": "0", "version": "1.0"
             }
    # data = {"method": method, "supplierCode": "300123", "requestId": str(uuid.uuid1()), "version": "1.0",
    #         "timestamp": 0, "data": json.dumps(dataData, separators=(',', ':'))}
    str2 = json.dumps(data, separators=(',', ':'))
    print(str2)
    data["sign"] = md5_sign(str2, "+YQIDAQAB")
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    res = requests.post(url=url, headers=headers, data=json.dumps(data, separators=(',', ':'))).text
    print(res)


update()
