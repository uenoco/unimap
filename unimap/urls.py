# -*- coding: utf-8 -*-
####
#   Unimap Project
####
"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from unimap import views

urlpatterns = [
    # 管理ページ
    path('admin/', admin.site.urls),

    # 暫定のトップページ
    path('', views.toppage, name='toppage'),

    # コース一覧ページ
    path('area', views.arealist, name='arealist'),
]


