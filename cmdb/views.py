from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
# Create your views here.


def index(request):
    return HttpResponse("连接nginx+uwsgi+django………………成功")


def interface(request):
    # return HttpResponse("接口调用成功")
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")