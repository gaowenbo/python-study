import pymysql
import pandas as pd
db = pymysql.connect(host="47.95.49.67",
                     port=8066,
                     user="sidb",
                     passwd="vFQ8nsab3Ia",
                     db="pay")

cur = db.cursor()
cur.execute("select * from zys_arrearage_order where arre_status = 1 and pay_type = 2 limit 99999999")
res = cur.fetchall()
print(list(cur.description))
fields = list(map(lambda x:list(x)[0], list(cur.description)))
print(fields)
df = pd.DataFrame(res, columns=fields)
df.to_excel("d:\\python\\target\\wxArr.xls")
import os
os.system("explorer.exe %s" % "/select,d:\\python\\target\\wxArr.xls")