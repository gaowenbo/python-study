from django.shortcuts import render
import pymysql

# Create your views here.

from django.http import HttpResponse, FileResponse
import datetime
import os

def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse(now)


def gitPull(request):
    os.system("GIT_DIR=/root/python-study/.git/ git pull");
    html = "<html><body>It is n3e</body></html>"
    return HttpResponse(html)

def wxArr(request):
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
    return HttpResponse("")