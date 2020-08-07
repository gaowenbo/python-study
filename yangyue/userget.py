import json
import pandas as pd

dic = json.loads(open("d:\\python\\source\\json2.txt", "r", encoding="utf-8").read())
arr = list(dic["records"])
arrNew = []


for a in arr:
    if a["ZCFZ"] != "0":
        a2 = []
        a2.append(a["ZZC"])
        a2.append(a["KHID"]["text"])
        a2.append(a["KHID"]["code"])
        a2.append(a["ZCFZ"])
        a2.append(a["YYJZRQ"])
        a2.append("\"" + a["KHID"]["text"] + "\",")
        arrNew.append(a2)


def getKey(a):
    print(a[3])
    zcfz = 0
    zzc = 0
    if (a[3] != ""):
        zcfz = float(a[3])
    if (a[0] != ""):
        zzc = float(a[0])
    return zzc * 100 + zcfz


arrNew = sorted(arrNew, key=lambda a: getKey(a), reverse=True)

df = pd.DataFrame(arrNew)
df.to_excel("d:\\python\\target\\exel2.xls")

print(arrNew)