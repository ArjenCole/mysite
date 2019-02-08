#!/usr/bin/env python
# -*-coding:utf-8-*-
from django.conf.urls import url
from django.contrib import admin
from bondcheck import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^/login', views.login),
    # 定义默认访问路由，表示输入任意url路径
    url(r'^$', views.wxBond),
]
