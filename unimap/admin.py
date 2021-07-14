####
#   Unimap Project
####
from django.contrib import admin
from django.contrib.gis import admin as geoadmin 
from . import models

# Register your models here.

#from unimap.models import Border, RecommendCourse
from unimap.models import Area, PointData

# Sightseeing route Area
class AreaAdmin(admin.ModelAdmin):
    list_display = ['Name', 'SubName', 'Booklet', 'DEF_LON', 'DEF_LAT' , 'DEF_Zoom' ]
admin.site.register(models.Area, AreaAdmin)

# Image Map (イラストマップ)
class ImageMapAdmin(admin.ModelAdmin):
    list_display = ['AreaId', 'ImageMap', 'LAT1', 'LON1', 'LAT2', 'LON2' ]
admin.site.register(models.ImageMap, ImageMapAdmin)

# Route
class RouteAdmin(admin.ModelAdmin):
    list_display = ['AreaId', 'Name', 'Summery', 'Sort' ]
admin.site.register(models.Route, RouteAdmin)
#admin.site.register(models.Route, geoadmin.OSMGeoAdmin)

# Point
class PointDataAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Sort', 'No', 'Summery', 'geom' ]
admin.site.register(models.PointData, geoadmin.OSMGeoAdmin)

#admin.site.register(models.PointData, geoadmin.OSMGeoAdmin)


# Slope
admin.site.register(models.Slope, geoadmin.OSMGeoAdmin)

# Zone
class ZoneAdmin(geoadmin.OSMGeoAdmin):
    list_display = ['Name', 'AreaId', 'Summery', 'Sort', 'Photo1' ]
admin.site.register(models.Zone, ZoneAdmin)
#admin.site.register(models.Zone, geoadmin.OSMGeoAdmin)

# Toilet
class ToiletAdmin(geoadmin.OSMGeoAdmin):
    list_display = ['Name','AreaId', 'Babyseat','Ostomate','Nursingbed','Washlet','Rotation','Emergencycall']
admin.site.register(models.Toilet, ToiletAdmin)
# admin.site.register(models.Toilet, geoadmin.OSMGeoAdmin)

# Hotel
class HotelAdmin(geoadmin.OSMGeoAdmin):
    list_display = ['Name','AreaId', 'TEL','Address']
admin.site.register(models.Hotel, HotelAdmin)
#admin.site.register(models.Hotel, geoadmin.OSMGeoAdmin)



