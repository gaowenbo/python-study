import openpyxl
import pymysql
from loguru import logger
import re
logger.add("d:\\python\\target\\seleniumdebug{time}.log", encoding="utf-8")
orderIds = [""];


str1 = 'orderId"2005181830659939", "2005181830663377", "2005161830574372","2005161830592303","2005161830592573","2005162515895666","2005162515889489","2005162515889879","2005162515893567","2005162515894683","2005162515894684","2005162515894738","2005172515901846","2005182515907285","2005152515883971","2005152515883865","2005151830541887","2005151830542602","2005152515881245","2005151830540896","2005152515880716"'
str2 = 'detailId"2005181832554116", "2005181832554517", "2005182515242742","2005172515243221","2005162515231301","2005162515232232","2005162515232155","2005162515232154","2005162515226978","2005162515222995","2005162515222450","2005161832467701","2005161832467375","2005161832447232""2005152515216578","2005152515216441","2005151832409595","2005151832407447","2005152515210297","2005151832405552","2005152515209737"'


db = pymysql.connect(host="47.95.49.67",
                     port=8066,
                     user="sidb",
                     passwd="vFQ8nsab3Ia",
                     db="pay")




cur = db.cursor()
cur.execute("select order_id, err_msg from zys_arrearage_order where pay_type = 2 and arre_status = 1 and fail_times > 10");
res = cur.fetchall()
# cur.execute("select shop_id,group_id from zys_shop_group limit 99999999")

di1 = list(res)

print("刷库语句")
for a in di1:
    print("update zhiyunshan_trade_order{}.zys_arrearage_order set fail_times = 4 where order_id = '{}';"
          .format(str(int(a[0][6:8]) + 1), a[0]));



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
