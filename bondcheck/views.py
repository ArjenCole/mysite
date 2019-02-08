from django.shortcuts import HttpResponse
from toollib import tools
from django.http import JsonResponse
import requests


def wxBond(request):
    resp = {'errorcode': 100, 'detail': 'wxBond'}
    return HttpResponse(tools.dicToJson(resp), content_type="application/json")


def test(request):
    resp = {'errorcode': 100, 'detail': 'test'}
    return HttpResponse(tools.dicToJson(resp), content_type="application/json")


def login(request):
    appid = 'wx1e6498038c6f6694'
    secret = '880ed1088abe49a31adcb3ec4d402c61'
    js_code = request.GET.get("code", None)
    url = 'https://api.weixin.qq.com/sns/jscode2session'
    t_data = {'appid': appid, 'secret': secret, 'js_code': js_code, 'grant_type': 'authorization_code'}
    # response = requests.post(url, data=t_data)
    # return HttpResponse(tools.strToJson(response.text), content_type="application/json")
    return JsonResponse(t_data)

