import requests
import json
import uuid
import time
def print1():
    # url = "https://api.weixin.qq.com/cgi-bin/template/api_add_template?access_token=33_CmZAvkDvhczqAdyeuQI99FkeOz8O2EXv8Y_BlUbnTixjCo7vOTKnHZdCFK892LfWvmFps-rT7ylIu1t-oeIYL4Zhqa_3rZ9L6xTNqno5Yw_OPz-W4sU9YUapX0qBn8V7PYOEOzSX355dK-uPOCJcADAKYF"
    # url = "https://api.weixin.qq.com/cgi-bin/template/api_set_industry?access_token=33_LYbFc8VtEaQ2ZHNZ8xzlu6IQv2rWjSkDN_VqsuQpM9Qz1ltq6MqjSUceJ1p2QaHzMCc2BLEjv-otgCA2hoqlHbxFLgwxIHjR8W-LZU-PXO3p_hqEAD0I6T08DwwfLqPMJvivd_YZIbhDysxpBNBjACARDR"
    url = "http://test-balanar.zhiyunshan.com/pay/api/v2/terminal/unkonwninfo/query?offLineId=LXNAP15219ctest1xxxxxxxx20041011001850523068"
    # url = "http://test-balanar.zhiyunshan.com//auth/api/v2/login?userCode=32228300050&password=888888&type=APP"
    data = {"offLineId": "8AE-0WhMevvIvOVqsHbNG6X5_ppsotCNstJ_ZnxLkRg"}
    # data = {"industry_id1": "2", "industry_id2": "10"}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyIwIjo1NzAsIjEiOiLliJjmgJ3oia8iLCJzdWIiOiI1NzAiLCIyIjpudWxsLCIzIjoyNjE2LCI0Ijo3NDIyLCI1Ijo4MDgyODEsIjYiOjIsIjciOiIzMjIyODMiLCI4Ijoi5YyX5Lqs5b6u5L-h5rWL6K-V5Y2B5LqU5LitIiwiOSI6Ium6u-i-o-eDqyIsImlhdCI6MTU5MTQ0NTcyMH0.Buuq8ro2g_kXbgwf6ts76dhyGS9Dp_9TE2NO_kJUW7w'}
    res = requests.post(url=url, headers=headers, data=json.dumps(data)).text
    print(res)

# LXNAP15219ctest1xxxxxxxx20041011001850523068
# LXNAP15219ctest1xxxxxxxx20041011013961114453
# LXNAP15219ctest1xxxxxxxx20041011021611828001
# LXNAP15219ctest1xxxxxxxx20041011024137365203

while True:
    print1()
    time.sleep(1)