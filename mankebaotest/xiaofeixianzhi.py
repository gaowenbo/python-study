import requests
import json
import uuid
import time
def prn1():
    # url = "https://api.weixin.qq.com/cgi-bin/template/api_add_template?access_token=33_CmZAvkDvhczqAdyeuQI99FkeOz8O2EXv8Y_BlUbnTixjCo7vOTKnHZdCFK892LfWvmFps-rT7ylIu1t-oeIYL4Zhqa_3rZ9L6xTNqno5Yw_OPz-W4sU9YUapX0qBn8V7PYOEOzSX355dK-uPOCJcADAKYF"
    # url = "https://api.weixin.qq.com/cgi-bin/template/api_set_industry?access_token=33_LYbFc8VtEaQ2ZHNZ8xzlu6IQv2rWjSkDN_VqsuQpM9Qz1ltq6MqjSUceJ1p2QaHzMCc2BLEjv-otgCA2hoqlHbxFLgwxIHjR8W-LZU-PXO3p_hqEAD0I6T08DwwfLqPMJvivd_YZIbhDysxpBNBjACARDR"
    urlF = "https://hb2-1.zysmul.zhiyunshan.com/pay/api/v2/terminal/order" \
          "info/pay?dinnerTypeName={}&userId={}&dinnerTypeId={}&" \
          "shopId={}&terminalParams={}&deviceSn={}&userNumber={}&medium={}&shopName={}&" \
          "noFoodAmount={}&userName={}&dinnerDate={}";
    # url = "http://test-balanar.zhiyunshan.com//auth/api/v2/login?userCode=32228300110&password=888888&type=APP"
    url= urlF.format("早餐", "1907240511366117", "104530", "40830", "shoudong", "G3C025Z2M19200064", "20190880070", "1", "南餐厅-教师窗口(新)", "800", "刘德印", "2020-06-04")
    print(url)
    data = {"deviceSn": "8AE-0WhMevvIvOVqsHbNG6X5_ppsotCNstJ_ZnxLkRg"}
    # data = {"industry_id1": "2", "industry_id2": "10"}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyIwIjo0MDEyNSwiMSI6IuWNl-mkkOWOhS3mlZnluIjnqpflj6Mo5pawKSIsInN1YiI6IjQwMTI1IiwiMiI6bnVsbCwiMyI6MTkwOCwiNCI6NDA4MzAsIjUiOjgwMjY0MywiNiI6MiwiNyI6IjEwMzY1MyIsIjgiOiLljZfpmLPluILnrKzkuIDkuK3lrabmoKEiLCI5Ijoi5Y2X6aSQ5Y6FLeaVmeW4iOeql-WPoyjmlrApIiwiaWF0IjoxNTkxMjc2MTI5fQ.DNK0UknkTW4658zcxAr_8dJXio5eH7Sje41262bHIug'}
    res = requests.post(url=url, headers=headers, data=json.dumps(data)).text
    print(res)

file = open("d:\\python\\source\\Untitled.txt", encoding="utf-8")

dinnerTypeName = []
userId = []
dinnerTypeId = []
shopId = []
terminalParams =[]
deviceSn =[]
userNumber =[]
medium =[]
shopName =[]
noFoodAmount =[]
userName =[]
dinnerDate =[]
orderId = []


while 1:
    line = file.readline()
    if line.__contains__("\"dinnerTypeName\":\""):
        dinnerTypeName.append(line)
    elif line.__contains__("\"userId\":\""):
        userId.append(line)
    elif line.__contains__("\"dinnerTypeId\":\""):
        dinnerTypeId.append(line)
    elif line.__contains__("\"shopId\":\""):
        shopId.append(line)
    elif line.__contains__("\"terminalParams\":\""):
        terminalParams.append(line)
    elif line.__contains__("\"deviceSn\":\""):
        deviceSn.append(line)
    elif line.__contains__("\"userNumber\":\""):
        userNumber.append(line)
    elif line.__contains__("\"medium\":\""):
        medium.append(line)
    elif line.__contains__("\"shopName\":\""):
        shopName.append(line)
    elif line.__contains__("\"noFoodAmount\":\""):
        noFoodAmount.append(line)
    elif line.__contains__("\"userName\":\""):
        userName.append(line)
    elif line.__contains__("\"dinnerDate\":\""):
        dinnerDate.append(line)
    elif line.__contains__("orderId"):
        orderId.append(line)
    if not line:
        break

# print(list(map(lambda x:x[113:129], orderId)))
orderId = list(map(lambda x:x[113:129], orderId))
dinnerTypeName = list(map(lambda x:x[57 + len("dinnerTypeName"):], dinnerTypeName))
userId = list(map(lambda x:x[57 + len("userId"):], userId))
dinnerTypeId = list(map(lambda x:x[57 + len("dinnerTypeId"):], dinnerTypeId))
shopId = list(map(lambda x:x[57 + len("shopId"):], shopId))
terminalParams = list(map(lambda x:x[57 + len("terminalParams"):], terminalParams))
deviceSn = list(map(lambda x:x[57 + len("deviceSn"):], deviceSn))
userNumber = list(map(lambda x:x[57 + len("userNumber"):], userNumber))
medium = list(map(lambda x:x[57 + len("medium"):], medium))
shopName = list(map(lambda x:x[57 + len("shopName"):], shopName))
noFoodAmount = list(map(lambda x:x[57 + len("noFoodAmount"):], noFoodAmount))
userName = list(map(lambda x:x[57 + len("userName"):], userName))
dinnerDate = list(map(lambda x:x[57 + len("dinnerDate"):], dinnerDate))

dinnerTypeName = list(map(lambda x:x[:-3], dinnerTypeName))
userId = list(map(lambda x:x[:-3], userId))
dinnerTypeId = list(map(lambda x:x[:-3], dinnerTypeId))
shopId = list(map(lambda x:x[:-3], shopId))
terminalParams = list(map(lambda x:x[:-3], terminalParams))
deviceSn = list(map(lambda x:x[:-3], deviceSn))
userNumber = list(map(lambda x:x[:-3], userNumber))
medium = list(map(lambda x:x[:-3], medium))
shopName = list(map(lambda x:x[:-3], shopName))
noFoodAmount = list(map(lambda x:x[:-3], noFoodAmount))
userName = list(map(lambda x:x[:-3], userName))
dinnerDate = list(map(lambda x:x[:-2], dinnerDate))
urlF = "https://hb2-1.zysmul.zhiyunshan.com/pay/api/v2/terminal/order" \
       "info/pay?dinnerTypeName={}&userId={}&dinnerTypeId={}&" \
       "shopId={}&terminalParams={}&deviceSn={}&userNumber={}&medium={}&shopName={}&" \
       "noFoodAmount={}&userName={}&dinnerDate={}";
# url = "http://test-balanar.zhiyunshan.com//auth/api/v2/login?userCode=32228300110&password=888888&type=APP"

# for i in range(0, 27):
#     url= urlF.format(dinnerTypeName[i], userId[i], dinnerTypeId[i], shopId[i], "shoudong", deviceSn[i], userNumber[i], medium[i], shopName[i], noFoodAmount[i], userName[i], dinnerDate[i])
#     print(url)
#     data = {"deviceSn": "8AE-0WhMevvIvOVqsHbNG6X5_ppsotCNstJ_ZnxLkRg"}
#     # data = {"industry_id1": "2", "industry_id2": "10"}
#     headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyIwIjo0MDEyNSwiMSI6IuWNl-mkkOWOhS3mlZnluIjnqpflj6Mo5pawKSIsInN1YiI6IjQwMTI1IiwiMiI6bnVsbCwiMyI6MTkwOCwiNCI6NDA4MzAsIjUiOjgwMjY0MywiNiI6MiwiNyI6IjEwMzY1MyIsIjgiOiLljZfpmLPluILnrKzkuIDkuK3lrabmoKEiLCI5Ijoi5Y2X6aSQ5Y6FLeaVmeW4iOeql-WPoyjmlrApIiwiaWF0IjoxNTkxMjc2MTI5fQ.DNK0UknkTW4658zcxAr_8dJXio5eH7Sje41262bHIug'}
#     res = requests.post(url=url, headers=headers, data=json.dumps(data)).text
#     print(res)

# print(dinnerTypeName)
# print(userId)
# print(dinnerTypeId)
# print(shopId)
# print(terminalParams)
# print(deviceSn)
# print(userNumber)
# print(medium)
# print(shopName)
# print(noFoodAmount)
# print(userName)
# print(dinnerDate)
# LXNAP15219ctest1xxxxxxxx20041011001850523068
# LXNAP15219ctest1xxxxxxxx20041011013961114453
# LXNAP15219ctest1xxxxxxxx20041011021611828001
# LXNAP15219ctest1xxxxxxxx20041011024137365203

prn1()
