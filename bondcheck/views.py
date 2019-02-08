from django.shortcuts import HttpResponse
from toollib import tools


def wxBond(request):
    resp = {'errorcode': 100, 'detail': 'wxBond'}
    return HttpResponse(tools.dicTojson(resp), content_type="application/json")


def login(request):
    resp = {'errorcode': 100, 'detail': 'login'}
    return HttpResponse(tools.dicTojson(resp), content_type="application/json")
