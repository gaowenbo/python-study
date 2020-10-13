



import requests
import pandas as pd
import json



def deleteOne(arr, token):
    suc = []
    # loginR = requests.post("http://mkb2test2.mankebao.cn/auth/api/v2/login?userCode=19919999291&password=xiyun123&type=MANAGER")
    # token = json.dumps(loginR.content.decode("utf-8"))
    # print(loginR.content.decode("utf-8"))
    # print(token)
    reserve = arr[::-1]
    for i in reserve[::-1]:
        headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': token}
        r = requests.post("https://canteen.sany.com.cn/base/api/v1/supplier/organise/delete?id={}".format(i), headers=headers)
        if r.status_code == 200:
            suc.append(i)
            reserve.remove(i)

        print(str(i) + r.content.decode("utf-8"))

    print("成功:" + str(suc))
    print("失败:" + str(reserve))


excel = pd.ExcelFile("d:\\python\\source\\待删除组织机构id.xlsx")
print(excel.sheet_names)
token = 'USER:313_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODQiLCJpYXQiOjE1OTc3NDUxMTR9.l8cx6GCzvIkxOyPigotfJKmfneZXs80QWkJZDyAdy9A'
excelName = "313-虚拟商户2"
data = excel.parse(sheet_name= excelName)
col=data.iloc[:,0]
arr = col.values.tolist()
print("处理" + excelName)
deleteOne(arr, token)

# url = "http://test-balanar.zhiyunshan.com/auth/api/v2/login?userCode=19919999291&password=xiyun123&type=MANAGER"

# for excelOne in excel.sheet_names:
#     data = excel.parse(sheet_name=excelOne)
#     col=data.iloc[:,0]
#     arr = col.values.tolist()
#     print("处理" + excelOne)
    # deleteOne(arr, token)