# coding=utf-8
import time
import hashlib
import requests
import json
import uuid
import sys
print(sys.getdefaultencoding())


printContent = '''
123456789a123456789a123456789a123456789a123456789a

一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十




'''

def str_to_bin(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

def bin2hex(bin):
    digital = "0123456789abcdef"
    sb = ""
    bs = bytearray(bin.encode("utf-8"))
    for i in bs:
        bit = (i & 0x0f0) >> 4;
        sb += digital[bit]
        bit = i & 0x0f
        sb += digital[bit]
    return sb

def str_to_hex(s):
    return ''.join([hex(ord(c)).replace('0x', '') for c in s])

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
appKey = "71684a8d36154cac8612ad17369683aa";
# sn = "N301P9BD40051"
sn = "N302P98S40164"
sn = "N301P9B940030"
def getSign(data):
    dataList = []
    for k in sorted(data):
        dataList.append(("%s=%s" %(k, data[k])))
    md5 = hashlib.md5()
    md5.update(("&".join(dataList) + appKey).encode(encoding='UTF-8'))
    return str(md5.hexdigest()).upper()


def printerAdd():

    url = "https://openapi.sunmi.com/v1/printer/printerAdd"
    data = {
          'app_id': "7b325307d92748aa99de5da44d7267cc",
          'msn': sn,
          'timestamp': int(round(time.time() * 1000)),
      'shop_id': "10089"
    }

    data['sign'] = getSign(data)
    res = requests.post(url=url, headers=headers, data=data).text
    print(res)

def printerUnbind():

    url = "https://openapi.sunmi.com/v1/printer/printerUnBind"
    data = {
        'app_id': "7b325307d92748aa99de5da44d7267cc",
        'msn': sn,
        'shop_id': "10089",
        'timestamp': int(round(time.time() * 1000))
    }

    data['sign'] = getSign(data)
    res = requests.post(url=url, headers=headers, data=data).text
    print(res)

def printerSearch():

    url = "https://openapi.sunmi.com/v1/machine/queryBindMachine"
    data = {
        'app_id': "7b325307d92748aa99de5da44d7267cc",
        'msn': sn,
        'timestamp': int(round(time.time() * 1000)),
        'shop_id': "400374"
    }
    data['sign'] = getSign(data)
    res = requests.post(url=url, headers=headers, data=data).text
    print(res)

def testPushPrint():

    m = "22486sdfaasdfgasg1648759098473225657849809写一篇文章吧...7867568796#$%^&*^%$%^&*^%$%^&*(*****f6a736f6e2{}{}248657861646连我"
    # for line in printContent.split("\n"):
    content = "0a".join(map(lambda a: bin2hex(a), printContent.split("\n")))

    url = "https://openapi.sunmi.com/v1/printer/pushContent"
    data = {
        'app_id': "7b325307d92748aa99de5da44d7267cc",
        'msn': sn,
        'timestamp': int(round(time.time() * 1000)),
        'pushId': str(uuid.uuid1()),
        'orderData': content
    }

    data['sign'] = getSign(data)
    res = requests.post(url=url, headers=headers, data=data).text
    print(res)

def queryPrint():

    url = "https://openapi.sunmi.com/v1/printer/getPrintStatus"
    data = {
        'app_id': "7b325307d92748aa99de5da44d7267cc",
        'msn': sn,
        'timestamp': int(round(time.time() * 1000)),
        'pushId': "dd2dd"
    }

    data['sign'] = getSign(data)
    res = requests.post(url=url, headers=headers, data=data).text
    print(res)

def pushVoice():
    url = "https://openapi.sunmi.com/v1/printer/pushVoice"
    data = {
        'app_id': "7b325307d92748aa99de5da44d7267cc",
        'msn': sn,
        'timestamp': int(round(time.time() * 1000)),
        'call_url': "https://yueyiwenhua.cn/assets/files/FuzaaiqOdRXrzwJXLDUCHZRY6g0T.mp3"
    }

    data['sign'] = getSign(data)
    res = requests.post(url=url, headers=headers, data=data).text
    print(res)

# queryPrint()
printerAdd()
# printerUnbind()
# testPushPrint()
# printerSearch()


