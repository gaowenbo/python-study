import requests
import json
import pandas as pd


def getinfo(startTime, endTime, payType):
    url = "https://zys.zhiyunshan.com/report/api/v1/reportOrderInfo/" \
        "getSupplierSaleAmountList?startDateTime="+str(startTime)+"&endDateTime=" +\
        str(endTime)+"&payType="+str(payType)
    headers = {'Content-Type': 'charset=utf8', 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                                                                '.eyJzdWIiOiIxIiwiaWF0IjoxNTgxMzE2OTYyfQ'
                                                                '.EZ7ga7K2PjP35Rf5b-J4XYtKkQPU2uuOK8yuNoxdyS8'}
    return requests.post(url=url, headers=headers).text


url = "https://zys.zhiyunshan.com/base/api/v1/supplier/list?supplierType=2&"\
    "limit=20000"
data = {"startDateTime": "1580745600000", "endDateTime": "1581264000000"}
headers = {'Content-Type': 'charset=utf8', 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                                                            '.eyJzdWIiOiIxIiwiaWF0IjoxNTgxMzE2OTYyfQ'
                                                            '.EZ7ga7K2PjP35Rf5b-J4XYtKkQPU2uuOK8yuNoxdyS8'}
res = requests.post(url=url, data=data, headers=headers)
text = json.loads(res.text)
supplierIdSet = set(map(lambda a: a["supplierId"], list(text["list"])))
print(supplierIdSet)
infosum = list()
for i in range(0, 40):
    a = 1546272000000 + i * 788400000
    b = 1546272000000 + (i + 1) * 788400000 - 1
    info = list(json.loads(getinfo(a, b, 3)))
    info = list(filter(lambda a: supplierIdSet.__contains__(a["supllierId"]), info))

    print(str(a) + "   " + str(b))
    print(info)
    for infoItem in info:
        infosum.append(list(dict(infoItem).values()))
name = ["1", "2", "3", "4", "5", "6", "7", "8"]
test = pd.DataFrame(columns=name, data=infosum)
grouped = test.groupby(['8'])
t = grouped.sum()
t.to_csv("d:\\python\\ss.csv", encoding="gbk")
print(infosum)
'''
startDateTime: 1580745600000
endDateTime: 1581264000000
supplierName:
supplierOperator:
payType: 1
supplierType:
orderSource: mankebaotest
retailEnable: 
'''