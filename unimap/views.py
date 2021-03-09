# -*- coding: utf-8 -*-
####
#   Unimap Project
####
import os
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .models import Area, PointData

# for Logging
#import logging

# 暫定トップページ
def toppage(request):
    return render(request, 'toppage.html')

# ロケーション一覧ページ
def arealist(request):
    try:
        # コースリストを取得
        arealist = Area.objects.all()
    except:
        arealist = ""
        
    params = { 'arealist': arealist }
    return render(request, 'area.html', params)

