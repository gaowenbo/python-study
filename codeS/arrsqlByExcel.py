import requests
import json
import uuid
import time
url = "http://localhost:31210/assistant/v1/yz/genSqlForOrder3?orderId={}&supplierId={}&payType={}"

def print1(one):
    # data = {"industry_id1": "2", "industry_id2": "10"}
    url2 = url.format(one[3], one[4], 2)
    # print(one)
    headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyIwIjo1ODQsIjEiOiLliJjmgJ3oia8iLCJzdWIiOiI1ODQiLCIyIjpudWxsLCIzIjoyNjE2LCI0Ijo3NTI4LCI1Ijo4MDgyODEsIjYiOjIsIjciOiIzMjIyODMiLCI4Ijoi5YyX5Lqs5b6u5L-h5rWL6K-V5Y2B5LqU5LitIiwiOSI6Iui_mOaYr-i1t-S4gOS4quavlOi-g-mVv-eahOWQjeensOadpea1i-ivleS4gOS4i-agt-W8j-mXrumimOWQp--8jOWlveeahCIsImlhdCI6MTU5MDg0NDkxOX0.Z24G-HmEBq0jAe2QUadXs1PZK6AAE4MroTUBeby_eBw'}
    res = requests.post(url=url2, headers=headers, data="").text
    print(res)

import pandas as pd

data = pd.read_excel("d:\\python\\source\\bb.xlsx")

for one in data.values:
    print1(one)

