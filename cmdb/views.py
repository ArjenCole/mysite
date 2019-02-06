from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models   # 引入数据库模型
import json
# Create your views here.


def index(request):
    if request.method == "POST":
        tname = request.POST.get("tname", None)
        tpassword = request.POST.get("tpassword", None)
        models.cmdb_new.objects.create(    # 数据库插入语句
            # mID=username,   # 设定字段与传入值进行对应（将会什么内容将会保存在什么字段下。）。
            mNAME=tname,
            mPASSWORD=tpassword,
        )
    user_list = models.cmdb_new.objects.all()     # 将数据全部展示至html中。
    return render(request, "index.html", {"user_list": user_list})
    # return render(request, "index.html")
    # return HttpResponse("连接nginx+uwsgi+django………………成功" + request.method)


def interface(request):
    if request.GET.get("interface", None) is None:
        return render(request, "index.html")

    operator = {
        'wxBondLogin': wxBondLogin,
        'wxBondGetTargets': wxBondGetTargetsn,
    }
    return operator.get(request.GET.get("interface", ""))(request.GET.get("x", ""),
                                                          request.GET.get("y", ""),
                                                          request.GET.get("z", ""))


def wxBondLogin(x, y, z):
    resp = {
        'errorcode': "success",
        'x': x
    }
    models.bond_userinfo.objects.create(  # 数据库插入语句
        # mID=username,   # 设定字段与传入值进行对应（将会什么内容将会保存在什么字段下。）。
        mNAME=x,
        mPASSWORD=y,
    )
    user_list = models.bond_userinfo.objects.all()
    return HttpResponse(json.dumps(user_list), content_type="application/json")


def wxBondGetTargetsn(x, y, z):
    resp = {
        'errorcode': "success",
        'y': y
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")