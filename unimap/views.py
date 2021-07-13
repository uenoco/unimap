# -*- coding: utf-8 -*-
####
#   Unimap Project
####
import os
import json
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

# Method for Class to JSON
def cj_method(item):
    if isinstance(item, object) and hasattr(item, '__dict__'):
        return item.__dict__
    else:
        raise TypeError

# マップ
def map(request,areaid):
    try:
        area  = Area.objects.get( id=areaid )
        image = ImageMap.objects.get( AreaId=areaid )

        #print( json.dumps(area, default=cj_method, indent=2))
        params = { "id":areaid, 'area': area, 'image': image }
        print( params )
        return render(request, 'map.html', params )
    except:
        return render(request, 'map.html'  )

