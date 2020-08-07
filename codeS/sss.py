import openpyxl
import pymysql
from loguru import logger
import re
logger.add("d:\\python\\target\\seleniumdebug{time}.log", encoding="utf-8")
orderIds = ["1910222011433113","1910282011454112","1912112011558112","1912182011572114","1912182011575113","1912192011571114","1912222011566114","1912242011567118","1912242011572118","1912272011587112","1912282011589113","1912302011589116","2006101011569113","2006251011579114","2006121412161116","2006162811937131","2006240511959135","2006240511960130","2007070511957184","2007080511955189","2004231211668137","2004231211668138","2001060611899122","2001060611901125","1912230011964129","1912260011960161","2001030012013115","2001030012020116","2001040012015120","2001120012058115","2001120012060114","2001120012063119","2001180012049138","2006140012125117","2007020012128165","2007030012129163","2007030012130176","2007050012132164","2007060012134160","2006243011956153","2006033112219135"];

for a in orderIds:
    print("update zhiyunshan_trade_order{}.zys_arrearage_order set fail_times = 8, ceil_order_id = '' where arre_id = '{}';"
          .format(str(int(a[6:8]) + 1), a));




#
# res2 = dict(filter(lambda x: not x[0] in di1.values(), res2))
#
# res4 = dict(filter(lambda x: not x[0] in di1))
# result = dict(zip(res2.keys(), map(lambda x: di1[x], res2.values())))
#
#
#
cur.close()
db.close()
logger.info(str(di1))


# def getComSql(key, param):
#     value1 = desList[1::]
#     value2 = desList[1::]
#     value2.append("e_dinner_id")
#     value1.append("e_dinner_id")
#     value2[9] = str(key)
#     print(value1)
#     sql = "INSERT INTO `zys_dinner_type_test2` (" + ','.join(value1) + ") select " + ','.join(value2) + " from " \
#                                                                                                         "zys_dinner_type_test2 where shop_id = " + str(param) + ";"
#     return sql
#

#
# f = open("d:\\python\\1.sql", "w", encoding="utf-8")
# for key in dict1.keys():
#     f.write(getComSql(key, dict1[key]) + "\n")
# f.close()
