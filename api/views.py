# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics,viewsets
from django.core.serializers import serialize

from unimap.models import Area, Toilet, Hotel, Zone, Route, PointData

# Create your views here.

    
def route(request, areaid):
    routeline = serialize('geojson', Route.objects.filter( AreaId=areaid ), geometry_field='geom', fields=('Sort','Name','Summery'))
    
    return HttpResponse( routeline, content_type='application/json')


def pointdata(request, areaid):
    routepoint = serialize('geojson', PointData.objects.filter( AreaId=areaid ), geometry_field='geom',
                           fields=('Sort','No','Name','Summery','Remarks','Open','Close','OpeningNote','Holiday','Price',
                                   'PriceNote','Discount','TEL','URL','Urltitle','Photo1','Photo2','Photo3','Photo360','Photo360_2',)
                           )
    
    return HttpResponse( routepoint, content_type='application/json')






