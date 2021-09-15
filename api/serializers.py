# -*- coding: utf-8 -*-
####
#   Project:      unimap
#   Applicattion: api/serializers.py
####
from rest_framework import serializers
from unimap.models import Toilet, Hotel, Zone, Route, PointData


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields=('Name','Summery','TEL','Address','Access','URL', 'Image1', 'Image2')
