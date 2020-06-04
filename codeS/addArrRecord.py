import requests
import json
import uuid
import time
import pymysql


db = pymysql.connect(host="47.95.49.67",
                     port=8066,
                     user="sidb",
                     passwd="vFQ8nsab3Ia",
                     db="pay")



cur = db.cursor()
ids = "'2005270822444217','2005270822444538','2005270822441999','2005270822445375','2005270822444818','2005270822445513','2005270822446915','2005270822451171','2005270822451172','2005272223229812','2005270032922236','2005270032920463','2005270032920851','2005270032922701','2005270032922780','2005270032921928','2005273026963677','2005273026966209','2005273026966625','2005273026967352','2005273026966838','2005271019290576','2005270523418749','2005270523421304','2005271831129231','2005271831130171','2005273026951821','2005273026951883','2005270523391917','2005272223217755','2005271831108212','2005271831108336','2005260822440663','2005262223214633','2005263026950849','2005260822438194','2005260822439582','2005260032888732','2005260032889912','2005263026942490','2005261831098275','2005261831098424','2005260822437406'"

cur.execute("select order_id, `supplier_id`, `buyer_id`, `buyer_name`, `shop_name`, `third_trade_no`, `pay_time`, `order_create_time`, `create_time`, `update_time`, `update_user_name`, `pay_type` from zys_order_info where order_id in ({})".format(ids));
res = cur.fetchall()
sqlf = "INSERT INTO `zhiyunshan_trade_order{}`.`zys_arrearage_order` (`arre_id`, `order_id`, `ceil_order_id`, " \
       "`suc_order_id`, `supplier_id`, `buyer_id`, `buyer_name`, `user_code`, `mobile`, `org_id`, " \
       "`org_name`, `org_code`, `org_full_code`, `arre_status`, `err_msg`, `exe_time`, `fail_times`, " \
       "`shop_name`, `third_trade_no`, `pay_time`, `order_create_time`, `create_time`, `update_time`, " \
       "`update_user_name`, `source`, `pay_type`, `arre_type`) VALUES " \
       "('{}', '{}', '', '', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '1', '6-2 手动补', '1589734800296', '4', '{}', '{}', '0', '{}', '2020-05-26 14:33:13', '2020-05-26 14:33:13', '', '0', '{}', '1');"

for one in res:
    db2 = pymysql.connect(host="47.95.49.67",
                         port=8066,
                         user="sidb",
                         passwd="vFQ8nsab3Ia",
                         db="base")
    cur2 = db2.cursor()
    cur2.execute("select `user_code`, `mobile`, `org_id`, `org_name`, `org_code`, `org_full_code` from zys_supplier_user where user_id = '{}';".format(one[2]));
    res2 = cur2.fetchall()
    # print(res2)
    arrsql = sqlf.format(str(int(one[0][6:8]) + 1), one[0], one[0], one[1], one[2], one[3], res2[0][0], res2[0][1], res2[0][2], res2[0][3], res2[0][4], res2[0][5], one[4], one[5], one[7], one[10])
    # print(arrsql)
    # print("update zhiyunshan_trade_order{}.zys_order_info set pay_status = 6 where order_id = '{}';".format(str(int(one[0][6:8]) + 1), one[0]))
    print("update zhiyunshan_trade_order{}.zys_arrearage_order set pay_type = 2 where order_id = '{}';".format(str(int(one[0][6:8]) + 1), one[0]))

print(res)

#"('1811132011298112', '1811132012331129', '', '', '1201', '1810222011297120', '李卫潮', '0904930', '', '145', '大学生', '1001503', '1001499-1001503-', '1', '补扣支付失败:101010125-支付失败，用户协议不存在，建议确认代扣业务传入的协议号对应的协议是否已解约。[AGREEMENT_NOT_EXIST]', '1589734800296', '90', '鑫考教育演示', '', '0', '1542090793509', '2018-11-13 14:33:13', '2018-11-13 14:33:13', '', '0', '1', '1');"

