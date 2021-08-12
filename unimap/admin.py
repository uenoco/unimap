####
#   Unimap Project
####
from django.contrib import admin
from django.contrib.gis import admin as geoadmin 
from . import models

# Register your models here.
from unimap.models import Area, ImageMap, Route, PointData, Zone, Toilet, Hotel

# Sightseeing route Area
class AreaAdmin(admin.ModelAdmin):
    list_display = ['DisplayOrder', 'Name', 'SubName', 'Booklet' ]
    list_display_links = [ 'Name', 'SubName' ]
    search_fields = [ 'Name', 'SubName' ]
    list_filter = [ 'Booklet' ]
#    ordering = [ 'DisplayOrder' ]
    ordering = [ 'id' ]
admin.site.register(models.Area, AreaAdmin)

# Image Map (イラストマップ)
class ImageMapAdmin(admin.ModelAdmin):
    list_display = ['AreaId', 'ImageMap', 'LAT1', 'LON1', 'LAT2', 'LON2' ]
admin.site.register(models.ImageMap, ImageMapAdmin)

# Route
class RouteAdmin(admin.ModelAdmin):
#class RouteAdmin(geoadmin.OSMGeoAdmin):
    list_display = ['AreaId', 'Sort' , 'Name', 'Summery' ]
    search_fields = [ 'Name', 'Summery' ]
    list_filter = ['AreaId', 'Sort' ]
admin.site.register(models.Route, RouteAdmin)
#admin.site.register(models.Route, geoadmin.OSMGeoAdmin)

# Point
class PointDataAdmin(admin.ModelAdmin):
    list_display = ['Name', 'AreaId', 'Sort', 'No', 'Summery' ]
    search_fields = [ 'Name', 'Summery' ]
    list_filter = ['AreaId', 'Sort' ]
admin.site.register(models.PointData, PointDataAdmin)

#admin.site.register(models.PointData, geoadmin.OSMGeoAdmin)

# Zone
class ZoneAdmin(geoadmin.OSMGeoAdmin):
    list_display = ['Name', 'AreaId', 'Summery', 'Sort' ]
    search_fields = [ 'Name', 'Summery' ]
    list_filter = ['AreaId', 'Sort' ]
admin.site.register(models.Zone, ZoneAdmin)

## WIP try Proxy
#class ZoneAdminProxy(admin.ModelAdmin):
#    list_display = ['Name', 'AreaId', 'Summery', 'Sort', 'Photo1' ]
#admin.site.register(ZoneAdminProxy)

# Toilet
class ToiletAdmin(geoadmin.OSMGeoAdmin):
    list_display = ['Name','AreaId', 'Babyseat','Ostomate','Nursingbed','Washlet','Rotation','Emergencycall']
    search_fields = [ 'Name' ]
admin.site.register(models.Toilet, ToiletAdmin)

# Hotel
class HotelAdmin(geoadmin.OSMGeoAdmin):
    list_display = ['Name','AreaId', 'TEL','Address']
    search = [ 'Name' ]
admin.site.register(models.Hotel, HotelAdmin)

# Booklet PDF
class BookletAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Publication', 'PDFfile' ]
    ordering = [ 'Publication' ]
admin.site.register(models.Booklet, BookletAdmin)

