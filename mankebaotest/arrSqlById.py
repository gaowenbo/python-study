import requests
import json
import uuid
import time
def print1():
    # url = "https://api.weixin.qq.com/cgi-bin/template/api_add_template?access_token=33_CmZAvkDvhczqAdyeuQI99FkeOz8O2EXv8Y_BlUbnTixjCo7vOTKnHZdCFK892LfWvmFps-rT7ylIu1t-oeIYL4Zhqa_3rZ9L6xTNqno5Yw_OPz-W4sU9YUapX0qBn8V7PYOEOzSX355dK-uPOCJcADAKYF"
    # url = "https://api.weixin.qq.com/cgi-bin/template/api_set_industry?access_token=33_LYbFc8VtEaQ2ZHNZ8xzlu6IQv2rWjSkDN_VqsuQpM9Qz1ltq6MqjSUceJ1p2QaHzMCc2BLEjv-otgCA2hoqlHbxFLgwxIHjR8W-LZU-PXO3p_hqEAD0I6T08DwwfLqPMJvivd_YZIbhDysxpBNBjACARDR"
    url = "http://test-balanar.zhiyunshan.com/pay/api/v2/terminal/unkonwninfo/query?offLineId=LXNAP15219ctest1xxxxxxxx20041011001850523068"
    # url = "http://test-balanar.zhiyunshan.com//auth/api/v2/login?userCode=32228300110&password=888888&type=APP"


    data = {"offLineId": "8AE-0WhMevvIvOVqsHbNG6X5_ppsotCNstJ_ZnxLkRg"}
    # data = {"industry_id1": "2", "industry_id2": "10"}
    headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyIwIjo1ODQsIjEiOiLliJjmgJ3oia8iLCJzdWIiOiI1ODQiLCIyIjpudWxsLCIzIjoyNjE2LCI0Ijo3NTI4LCI1Ijo4MDgyODEsIjYiOjIsIjciOiIzMjIyODMiLCI4Ijoi5YyX5Lqs5b6u5L-h5rWL6K-V5Y2B5LqU5LitIiwiOSI6Iui_mOaYr-i1t-S4gOS4quavlOi-g-mVv-eahOWQjeensOadpea1i-ivleS4gOS4i-agt-W8j-mXrumimOWQp--8jOWlveeahCIsImlhdCI6MTU5MDg0NDkxOX0.Z24G-HmEBq0jAe2QUadXs1PZK6AAE4MroTUBeby_eBw'}
    res = requests.post(url=url, headers=headers, data=json.dumps(data)).text
    print(res)

# LXNAP15219ctest1xxxxxxxx20041011001850523068
# LXNAP15219ctest1xxxxxxxx20041011013961114453
# LXNAP15219ctest1xxxxxxxx20041011021611828001
# LXNAP15219ctest1xxxxxxxx20041011024137365203

while True:
    print1()
    time.sleep(1)