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
from .models import Area, ImageMap, Route, PointData, Toilet, Hotel

# Ffor Logging
import logging


# トップページ
def toppage(request):
    try:
        arealist = Area.objects.all()
    except:
        arealist = ""
    params = { 'arealist': arealist }

    return render(request, 'toppage.html', params)

# エリア一覧
def arealist(request):
    try:
        arealist = Area.objects.all()
    except:
        arealist = ""
    params = { 'arealist': arealist }
    return render(request, 'area.html', params)

# テストトップページ
def test(request):
    return render(request, 'test.html')

# マップ
def map(request,areaid):
    print( "----  map in views.py-----" )
    try:
        # get areaId
        area  = Area.objects.get( id=areaid )
        # set ImageMap
        image = ImageMap.objects.get( AreaId=area.id )
        mediaURL = settings.MEDIA_URL        # image Bacs-URL
        # set route
        #route = route.objects.get( AreaId=area.id )

        #print( json.dumps(area, default=cj_method, indent=2))
        params = { 'imagemap': image, 'mediaurl': mediaURL }
        #print( area.id )
        #print( params )
        
        print( "----  return in views.py-----" )
        return render(request, 'map.html', params )
    except:
        return render(request, 'map.html'  )

# Method for Class to JSON
def cj_method(item):
    if isinstance(item, object) and hasattr(item, '__dict__'):
        return item.__dict__
    else:
        raise TypeError

