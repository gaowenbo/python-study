from django.shortcuts import render
import pymysql
import requests
# Create your views here.

from django.http import HttpResponse, FileResponse
import datetime
import os

def current_datetime(request):
    now = datetime.datetime.now().timestamp()
    return HttpResponse(now)


def gitPull(request):
    os.system("GIT_DIR=/root/python-study/.git/ git pull");
    html = "<html><body>It is n3e</body></html>"
    return HttpResponse(html)

def wxOpen(request):

    data = {
                    "appid": 'wxf88cbbf220e72ba5',
                    "secret": '60f06a66c1f425b1883dd4381d728ecb',
                    "code":  request.GET.get('code', "0")
                }
    res = requests.get(url="https://api.weixin.qq.com/sns/jscode2session?appId=wxf88cbbf220e72ba5", data=data).text
    # db = pymysql.connect(host="47.95.49.67",
    #                      port=8066,
    #                      user="sidb",
    #                      passwd="vFQ8nsab3Ia",
    #                      db="pay")
    #
    # cur = db.cursor()
    # cur.execute("select * from zys_arrearage_order where arre_status = 1 and pay_type = 2 limit 99999999")
    # res = cur.fetchall()
    # print(list(cur.description))
    # fields = list(map(lambda x:list(x)[0], list(cur.description)))
    # print(fields)
    # df = pd.DataFrame(res, columns=fields)
    # df.to_excel("wxArr.xls")
    # file = open('wxArr.xls', 'rb')
    # response = FileResponse(file)
    # response['Content-Type'] = 'application/octet-stream'
    # response['Content-Disposition'] = 'attachment;filename="wxArr.xls"'
    return HttpResponse(res)