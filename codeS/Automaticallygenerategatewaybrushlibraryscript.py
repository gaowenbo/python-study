

#start
appCurrentId = 36
currentId = 1022
serviceCurrentId = 433

supplierName="太原同创谷"
supplierId="860659"
ip="1.71.191.55"

import random,string
src_digits = string.digits              #string_数字
src_uppercase = string.ascii_uppercase  #string_大写字母
src_lowercase = string.ascii_lowercase  #string_小写字母
digits_num = random.randint(3,6)
uppercase_num = random.randint(3,6)
lowercase_num = random.randint(3,6)

#生成字符串
password = random.sample(src_digits,digits_num) + random.sample(src_uppercase,uppercase_num) + random.sample(src_lowercase,lowercase_num)

#打乱字符串
random.shuffle(password)

md5=''.join(password)
appCurrentId = appCurrentId+1
currentId = currentId+1

print("INSERT INTO `gateway`.`open_app` (`open_supplier_id`, `supplier_id`, `supplier_code`, `supplier_name`, `open_status`, `open_public_key`, `open_private_key`, `supplier_public_key`, `supplier_private_key`, `open_white`, `create_time`, `create_user_id`, `create_user_name`, `update_time`, `update_user_id`, `update_user_name`, `md5_key`, `sign_type`) VALUES ('{}', '{}', '{}', '{}', '1', '', '', '', '', '123.181.238.35,{}', NULL, NULL, NULL, NULL, NULL, NULL, '{}', '2');".
      format(appCurrentId, supplierId, currentId, supplierName, ip, md5))
serviceCurrentId=serviceCurrentId+1
print("INSERT INTO `gateway`.`service_app` (`service_id`, `open_supplier_id`, `api_id`, `api_limiting`, `create_time`, `last_update_time`, `api_method`) VALUES ('{}', '{}', '0', '0', NULL, '2020-06-15 16:21:23', 'test');".
      format(serviceCurrentId, appCurrentId))
serviceCurrentId=serviceCurrentId+1
print("INSERT INTO `gateway`.`service_app` (`service_id`, `open_supplier_id`, `api_id`, `api_limiting`, `create_time`, `last_update_time`, `api_method`) VALUES ('{}', '{}', '0', '0', NULL, '2020-06-15 16:21:23', 'ks.facefeature.get');".
      format(serviceCurrentId, appCurrentId))
serviceCurrentId=serviceCurrentId+1
print("INSERT INTO `gateway`.`service_app` (`service_id`, `open_supplier_id`, `api_id`, `api_limiting`, `create_time`, `last_update_time`, `api_method`) VALUES ('{}', '{}', '0', '0', NULL, '2020-06-15 16:21:23', 'ks.facefeature.detect');".
      format(serviceCurrentId, appCurrentId))


print(supplierName);
print("zqsy:");
print("  gateway:");
print("    appId: {}".format(currentId));
print("    md5Key: {}".format(md5));
print("    serverUrl: https://gateway.mankebao.cn")


