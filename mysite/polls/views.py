from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime
import os

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is nows %s.</body></html>" % now
    return HttpResponse(html)


def gitPull(request):
    os.system("GIT_DIR=/root/python-study/.git/ git pull");
    html = "<html><body>It is n3</body></html>"
    return HttpResponse(html)