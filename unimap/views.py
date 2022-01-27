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
from .models import Area, ImageMap, Route, PointData, Toilet, Hotel, Booklet

# Ffor Logging
import logging


# トップページ
def toppage(request):
    try:
        arealist = Area.objects.filter( DisplayFlag=True ).order_by('DisplayOrder')
        bookletlist = Booklet.objects.all().order_by('id')
    except:
        arealist = ""
        bookletlist = ""
    mediaURL = settings.MEDIA_URL        
    params = { 'arealist': arealist,'bookletlist': bookletlist, 'mediaurl': mediaURL }

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
    #print( areaid )
    try:
        # get arealist
        arealist = Area.objects.filter( DisplayFlag=True ).order_by('DisplayOrder')

        # get target area
        area  = Area.objects.get( id=areaid )
    except:
        return render(request, 'map.html'  )

    try:
        # get ImageMap
        imap = ImageMap.objects.get( AreaId=areaid )
        mediaURL = settings.MEDIA_URL        
        # set route/point
        #route = route.objects.get( AreaId=area.id )
        #point = point.objects.get( AreaId=area.id )

        params = { 'arealist':arealist, 'area':area, 'imagemap': imap, 'mediaurl': mediaURL }
        #print( areaid )
        return render(request, 'map.html', params )
    except:
        params = { 'arealist':arealist, 'area':area }
        #print( areaid )
        return render(request, 'map.html', params )

# マップ
def hotel(request,hotelid):
    #print( hotelid )
    try:
        # get hotel-detail
        hotel = Hotel.objects.get( id=hotelid )

        params = { 'hotel':hotel }
        #print( areaid )
        return render(request, 'hotel_detail.html', params )
    except:
        return render(request, 'hotel_detail.html'  )

# Method for Class to JSON
def cj_method(item):
    if isinstance(item, object) and hasattr(item, '__dict__'):
        return item.__dict__
    else:
        raise TypeError

