# -*- coding: utf-8 -*-
####
#   Project:      unimap
#   Applicattion: api
####
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from djgeojson.views import GeoJSONLayerView
from unimap.models import Toilet, Hotel, Zone, Route, PointData

from api import views

urlpatterns = [
    #path('', include(router.urls)),
    path('v1/toilet.geojson',GeoJSONLayerView.as_view(
        model=Toilet,
        properties=['Name','Summery','Floor','Babyseat','Ostomate','Nursingbed','Washlet','Rotation','Emergencycall',
                    'Photo1','Photo2','Photo3','Photo360','Photo360_2']
    ), name='toilet'),

    path('v1/hotel.geojson',GeoJSONLayerView.as_view(
        model=Hotel,
        properties=['Name','Summery','TEL','Address','Access','URL','URL_f21',
                    'Photo1','Photo2','Photo3','Photo360','Photo360_2']
    ), name='hotel'),

    path('v1/zone.geojson',GeoJSONLayerView.as_view(
        model=Zone,
        properties=['Name','Summery','Sort', 'Photo1','Photo2','Photo3','Photo360','Photo360_2']
    ), name='zone'),

    # Course Route :LineString
    path('v1/route.geojson',GeoJSONLayerView.as_view(
        model=Route,
        properties=['AreaId','Sort','Name','Summery']
    ), name='route'),

    # Course Route bu AreaId
    path('v1/route/<int:areaid>', views.route, name='route'),
    
    # Course PointData
    path('v1/point.geojson',GeoJSONLayerView.as_view(
        model=PointData,
        properties=['AreaId','Sort','No','Name','Summery','Remarks','Open','Close','OpeningNote',
                    'Holiday','Price','PriceNote','Discount','TEL','URL','Urltitle',
                    'Photo1','Photo2','Photo3','Photo360','Photo360_2']
    ), name='point'),
    # Course Route bu AreaId
    path('v1/point/<int:areaid>', views.pointdata, name='pointdata'),
]

