from django.shortcuts import HttpResponse
from cmdb import models   # 引入数据库模型
from cmdb import tools


def wxBond(request):
    resp = {'errorcode': 100, 'detail': 'wxBond'}
    return HttpResponse(tools.dicTojson(resp), content_type="application/json")


def login(request):
    resp = {'errorcode': 100, 'detail': 'login'}
    return HttpResponse(tools.dicTojson(resp), content_type="application/json")
