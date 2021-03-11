# -*- coding: utf-8 -*-
####
#   Unimap Project
####
import os
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

# Database Tables
from .models import Area, ImageMap, Route, PointData, Slope, Toilet, Hotel

# Ffor Logging
import logging


# 暫定トップページ
def toppage(request):
    return render(request, 'toppage.html')

# エリア一覧
def arealist(request):
    try:
        arealist = Area.objects.all()
    except:
        arealist = ""
    params = { 'arealist': arealist }
    return render(request, 'area.html', params)

# マップ
def map(request,areaid):
    area  = Area.objects.get( id=areaid )
    image = ImageMap.objects.get( AreaId=areaid )
    params = { 'area':area, 'image': image } 
    return render(request, 'map.html', params )


