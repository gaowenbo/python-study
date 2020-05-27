import requests
import json
import uuid


url = "https://api.weixin.qq.com/cgi-bin/template/api_add_template?access_token=33_CmZAvkDvhczqAdyeuQI99FkeOz8O2EXv8Y_BlUbnTixjCo7vOTKnHZdCFK892LfWvmFps-rT7ylIu1t-oeIYL4Zhqa_3rZ9L6xTNqno5Yw_OPz-W4sU9YUapX0qBn8V7PYOEOzSX355dK-uPOCJcADAKYF"
# url = "https://api.weixin.qq.com/cgi-bin/template/api_set_industry?access_token=33_LYbFc8VtEaQ2ZHNZ8xzlu6IQv2rWjSkDN_VqsuQpM9Qz1ltq6MqjSUceJ1p2QaHzMCc2BLEjv-otgCA2hoqlHbxFLgwxIHjR8W-LZU-PXO3p_hqEAD0I6T08DwwfLqPMJvivd_YZIbhDysxpBNBjACARDR"
url = "https://api.weixin.qq.com/cgi-bin/template/del_private_template?access_token=33_u_qPrwtxQ_GJKkxEXUlvKNIXv2uZe8Ly6rWH1TbXbXLxpmw2bLFSzYFdB-p6_UeZJGDL2wHSbVl1j_GSp7kHaukQiMrXpnDtaA5Knr-xZCOog-WWXw_BC06suz-6vMmfzOdQalUWoM76C-j6SSQbAHAEEC"

data = {"template_id": "8AE-0WhMevvIvOVqsHbNG6X5_ppsotCNstJ_ZnxLkRg"}
# data = {"industry_id1": "2", "industry_id2": "10"}
headers = {'Content-Type': 'application/json; charset=utf-8'}
res = requests.post(url=url, headers=headers, data=json.dumps(data)).text

print(res)

res = requests.post(url="https://server.yueyiwenhua.cn/push", headers=headers).text