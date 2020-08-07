import requests
import json
import uuid
import time
def test():
    # url = "https://api.weixin.qq.com/cgi-bin/template/api_add_template?access_token=33_CmZAvkDvhczqAdyeuQI99FkeOz8O2EXv8Y_BlUbnTixjCo7vOTKnHZdCFK892LfWvmFps-rT7ylIu1t-oeIYL4Zhqa_3rZ9L6xTNqno5Yw_OPz-W4sU9YUapX0qBn8V7PYOEOzSX355dK-uPOCJcADAKYF"
    # url = "https://api.weixin.qq.com/cgi-bin/template/api_set_industry?access_token=33_LYbFc8VtEaQ2ZHNZ8xzlu6IQv2rWjSkDN_VqsuQpM9Qz1ltq6MqjSUceJ1p2QaHzMCc2BLEjv-otgCA2hoqlHbxFLgwxIHjR8W-LZU-PXO3p_hqEAD0I6T08DwwfLqPMJvivd_YZIbhDysxpBNBjACARDR"
    # url = "http://test-balanar.zhiyunshan.com/pay/api/v2/terminal/unkonwninfo/query?offLineId=LXNAP15219ctest1xxxxxxxx20041011001850523068"
    # url = "http://test-balanar.zhiyunshan.com/auth/api/v2/login?userCode=19919999291&password=xiyun123&type=MANAGER"
    url = "http://test-balanar.zhiyunshan.com/report/api/v1/reportUserOrderInfo/list?dinnerDate=1592841600000&orgId=&shopId=&dinnerType"
    # url = "http://localhost:12800/report/api/v1/reportUserOrderInfo/list?dinnerDate=1592841600000&orgId=&shopId=&dinnerType"
    url = "http://localhost:12800/report/api/v1/reportUserOrderInfo/detail?dinnerDate=1592841600000&orgId=16056&shopId=&dinnerType=25,35"
    # url = "http://test-balanar.zhiyunshan.com/auth/api/v2/login?userCode=19919999291&password=xiyun123&type=MANAGER"

    data = {"offLineId": "8AE-0WhMevvIvOVqsHbNG6X5_ppsotCNstJ_ZnxLkRg"}
    # data = {"industry_id1": "2", "industry_id2": "10"}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1ODgwIiwiaWF0IjoxNTkzNjcxMzI5fQ.-W8HB0WjYhJI_-0KH1mlHMHIp4R7fykTrcjSkcVmJ1Q'}
    res = requests.post(url=url, headers=headers, data=json.dumps(data)).text
    print(res)

def test2():
    # url = "https://api.weixin.qq.com/cgi-bin/template/api_add_template?access_token=33_CmZAvkDvhczqAdyeuQI99FkeOz8O2EXv8Y_BlUbnTixjCo7vOTKnHZdCFK892LfWvmFps-rT7ylIu1t-oeIYL4Zhqa_3rZ9L6xTNqno5Yw_OPz-W4sU9YUapX0qBn8V7PYOEOzSX355dK-uPOCJcADAKYF"
    # url = "https://api.weixin.qq.com/cgi-bin/template/api_set_industry?access_token=33_LYbFc8VtEaQ2ZHNZ8xzlu6IQv2rWjSkDN_VqsuQpM9Qz1ltq6MqjSUceJ1p2QaHzMCc2BLEjv-otgCA2hoqlHbxFLgwxIHjR8W-LZU-PXO3p_hqEAD0I6T08DwwfLqPMJvivd_YZIbhDysxpBNBjACARDR"
    # url = "http://test-balanar.zhiyunshan.com/pay/api/v2/terminal/unkonwninfo/query?offLineId=LXNAP15219ctest1xxxxxxxx20041011001850523068"
    # url = "http://test-balanar.zhiyunshan.com/auth/api/v2/login?userCode=19919999291&password=xiyun123&type=MANAGER"
    url = "http://localhost:8030/food/api/v1/checker/list"
    # url = "http://test-balanar.zhiyunshan.com/auth/api/v2/login?userCode=19919999291&password=xiyun123&type=MANAGER"

    data = {"offLineId": "8AE-0WhMevvIvOVqsHbNG6X5_ppsotCNstJ_ZnxLkRg"}
    # data = {"industry_id1": "2", "industry_id2": "10"}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'USER:301_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1MzIiLCJpYXQiOjE1OTUzMTY0NzF9.HgwP6wLpPbkgVnsZlWQ-bRKy2vvWJvD2fycDjJMhoww'}
    res = requests.post(url=url, headers=headers, data=json.dumps(data)).text
    print(res)

# LXNAP15219ctest1xxxxxxxx20041011001850523068
# LXNAP15219ctest1xxxxxxxx20041011013961114453
# LXNAP15219ctest1xxxxxxxx20041011021611828001
# LXNAP15219ctest1xxxxxxxx20041011024137365203

test2()