import requests
import json
import uuid
import time
import pymysql
import pandas as pd

db = pymysql.connect(host="47.95.49.67",
                     port=8066,
                     user="sidb",
                     passwd="vFQ8nsab3Ia",
                     db="pay")

cur = db.cursor()
# 2704
cur.execute("select buyer_id,buyer_name,org_name,err_msg,exe_time,create_time from zys_arrearage_order where arre_status = 1 and pay_type = 2 and supplier_id = {} limit 99999999".format(2704))
res = cur.fetchall()


def getMobile(param):
    db2 = pymysql.connect(host="47.95.49.67",
                         port=8066,
                         user="sidb",
                         passwd="vFQ8nsab3Ia",
                         db="base")

    cur2 = db2.cursor()
    cur2.execute("select face_linkman_mobile from zys_supplier_user where user_id = '{}'".format(param))
    res2 = cur2.fetchall()
    return res2[0][0]

resNew = []
for s in res:
    sN = list(s)
    if sN[4] == 0:
        sN[4] = s[5]
    else:
        sN[4] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(sN[4]/1000))
   # sN.append(getMobile(s[0]))
    sN[5] = getMobile(s[0])
    resNew.append(sN)
print(list(cur.description))
fields = ["userId", "姓名", "班级", "扣款失败原因", "最后一次扣款时间", "联系人手机号"]
print(fields)
df = pd.DataFrame(resNew, columns=fields)
df.to_excel("d:\\python\\target\\黑龙江伊春市第一中学8-12.xlsx")

