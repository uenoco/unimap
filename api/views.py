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
def route(request, areaid):
    routeline = serialize('geojson', Route.objects.filter( AreaId=areaid ), geometry_field='geom', fields=('Sort','Name','Summery'))
    
    return HttpResponse( routeline, content_type='application/json')

def pointdata(request, areaid):
    routepoint = serialize('geojson', PointData.objects.filter( AreaId=areaid ), geometry_field='geom',
                           fields=('Sort','No','Name','Summery','Remarks','Open','Close','OpeningNote','Holiday','Price',
                                   'PriceNote','Discount','TEL','URL','Urltitle','Photo1','Photo2','Photo3','Photo360','Photo360_2')
                           )
    return HttpResponse( routepoint, content_type='application/json')


@property
def get_absolute_image1_url(self):
    return "{0}{1}".format(MEDIA_URL, self.Image1.url)

def hoteldata(request):
    hotels=Hotel.objects.all()
    print(hotels)
    hotelpoint = serialize('geojson', Hotel.objects.all(), geometry_field='geom',
                           fields=('pk','Name','Summery','TEL','Address','Access','URL','URL_f21','Image1', 'Image2')
                           )
    print( hotelpoint )
    return HttpResponse( hotelpoint, content_type='application/json')

