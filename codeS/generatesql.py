

strs = open("d:\\python\\source\\补扣.txt", "r", encoding="utf-8").readlines()

c = "INSERT INTO `pay`.`zys_arrearage_order` (`arre_id`, `order_id`, `ceil_order_id`, `suc_order_id`, `supplier_id`, `buyer_id`, `buyer_name`, `user_code`, `mobile`, `org_id`, `org_name`, `org_code`, `org_full_code`, `arre_status`, `err_msg`, `exe_time`, `fail_times`, `shop_name`, `third_trade_no`, `pay_time`, `order_create_time`, `create_time`, `update_time`, `update_user_name`, `source`, `pay_type`) VALUES ('"

file = open("d:\\python\\target\\补扣.txt", "w", encoding="utf-8")
for ss in strs:
    s = "update {}.zys_arrearage_order set {} = 2 where arre_id = {} and fail_times > 40;"
    ss = ss[len(c):len(c) + 16]
    route = int(ss[7:8])
    file.write(s.format("zhiyunshan_trade_order" + str((route + 1)), "fail_times", "\"" + ss + "\"" ) + "\n")

    print(s.format("zhiyunshan_trade_order" + str((route + 1)), "fail_times", "\"" + ss + "\"" ))
file.close()