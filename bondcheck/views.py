from django.shortcuts import HttpResponse
from toollib import tools
import requests
import json


def wxBond(request):
    resp = {'errorcode': 100, 'detail': 'wxBond'}
    return HttpResponse(tools.dicTojson(resp), content_type="application/json")


def test(request):
    resp = {'errorcode': 100, 'detail': 'test'}
    return HttpResponse(tools.dicTojson(resp), content_type="application/json")

def login(request):
    '''
    resp = {'errorcode': 100, 'detail': 'login'}
    return HttpResponse(tools.dicTojson(resp), content_type="application/json")
    '''
    appid = 'wx1e6498038c6f6694'
    secret = '880ed1088abe49a31adcb3ec4d402c61'
    js_code = request.GET.get("code", None)
    url = 'https://api.weixin.qq.com/sns/jscode2session?'
    url += 'appid=' + appid + '&secret=' + secret + '&js_code=' + js_code +'&grant_type=authorization_code'
    response = requests.post(url)
    # return response
    return HttpResponse(url)

