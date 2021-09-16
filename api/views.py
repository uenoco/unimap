# -*- coding: utf-8 -*-
from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize

from rest_framework import generics,viewsets
from rest_framework.response import Response
from rest_framework import status

from unimap.settings import MEDIA_URL
from unimap.models import Area, Toilet, Hotel, Zone, Route, PointData

#from rest_framework.decorators import api_view, renderer_classes
#from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

#from .serializers import HotelSerializer

import json

# Create your views here.
# route by areaid
def route(request, areaid):
    routeline = serialize('geojson', Route.objects.filter( AreaId=areaid ), geometry_field='geom', fields=('Sort','Name','Summery'))
    return HttpResponse( routeline, content_type='application/json')

# routepoint by areaid
def routepointdata(request, areaid):
    routepoint = serialize('geojson', PointData.objects.filter( AreaId=areaid ), geometry_field='geom',
                           fields=('Sort','No','Name','Summery','Remarks','Open','Close','OpeningNote','Holiday','Price',
                                   'PriceNote','Discount','TEL','URL','Urltitle',
                                   'Image1','image2','Photo1','Photo2','Photo360')
                           )
    return HttpResponse( routepoint, content_type='application/json')

# pointdata
def pointdata(request):
    routepoint = serialize('geojson', PointData.objects.all(), geometry_field='geom',
                           fields=('Sort','No','Name','Summery','Remarks','Open','Close','OpeningNote','Holiday','Price',
                                   'PriceNote','Discount','TEL','URL','Urltitle',
                                   'Image1','image2','Photo1','Photo2','Photo360')
                           )
    return HttpResponse( routepoint, content_type='application/json')

# zone for pass
def zonedata(request):
    zonepolygon = serialize('geojson', Zone.objects.all(), geometry_field='geom',
                           fields=('Sort','Name','Summery','Image1', 'Image2', 'Photo1', 'Photo2','Photo360')
                           )
    #print( hotelpoint )
    return HttpResponse( zonepolygon, content_type='application/json')

def hoteldata(request):
    #hotels=Hotel.objects.all()
    #print(hotels)
    hotelpoint = serialize('geojson', Hotel.objects.all(), geometry_field='geom',
                           fields=('pk','Name','Summery','TEL','Address','Access','URL','URL_f21','Image1', 'Image2')
                           )
    #print( hotelpoint )
    return HttpResponse( hotelpoint, content_type='application/json')

def toiletdata(request):
    #toilets=Toilet.objects.all()
    #print(toiletss)
    toiletpoint = serialize('geojson', Toilet.objects.all(), geometry_field='geom',
                            fields=('Name','Summery','Floor',
                                    'Babyseat','Ostomate','Nursingbed','Washlet','Rotation','Emergencycall',
                                    'Image1', 'Image2', 'Photo1','Photo2','Photo360')
                           )
    #print( toiletpoint )
    return HttpResponse( toiletpoint, content_type='application/json')

