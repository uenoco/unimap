####
#   Unimap Project
####
from django.contrib import admin
from django.contrib.gis import admin as geoadmin 
from . import models

# import_export 
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

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

# Route import_export
class RouteResource(resources.ModelResource):
    ordering = [ 'id' ]
    class Meta:
        model = Route
class RouteAdmin(geoadmin.OSMGeoAdmin,ImportExportModelAdmin):
    list_display = ['AreaId', 'Sort' , 'Name', 'Summery' ]
    search_fields = [ 'Name', 'Summery' ]
    list_filter = ['AreaId', 'Sort' ]
    ordering = [ 'AreaId', 'id' ]
    resource_class = RouteResource
    formats = [base_formats.CSV]
admin.site.register(models.Route, RouteAdmin)

# PointData import_export
class PointResource(resources.ModelResource):
    class Meta:
        model = PointData
class PointDataAdmin(geoadmin.OSMGeoAdmin,ImportExportModelAdmin):
    list_display = ['Name', 'AreaId', 'Sort', 'No' ]
    search_fields = [ 'Name', 'Summery' ]
    list_filter = ['AreaId', 'Sort' ]
    resource_class = PointResource
    formats = [base_formats.CSV]
admin.site.register(models.PointData, PointDataAdmin)

#admin.site.register(models.PointData, geoadmin.OSMGeoAdmin)

# Zone import_export
class ZoneResource(resources.ModelResource):
    class Meta:
        model = Zone
class ZoneAdmin(geoadmin.OSMGeoAdmin,ImportExportModelAdmin):
    list_display = ['Name', 'AreaId', 'Summery', 'Sort' ]
    search_fields = [ 'Name', 'Summery' ]
    list_filter = ['AreaId', 'Sort' ]
    resource_class = ZoneResource
    formats = [base_formats.CSV]
admin.site.register(models.Zone, ZoneAdmin)
        
## WIP try Proxy
#class ZoneAdminProxy(admin.ModelAdmin):
#    list_display = ['Name', 'AreaId', 'Summery', 'Sort', 'Photo1' ]
#admin.site.register(ZoneAdminProxy)

# Toilet import_export
class ToiletResource(resources.ModelResource):
    class Meta:
        model = Toilet
class ToiletAdmin(geoadmin.OSMGeoAdmin,ImportExportModelAdmin):
    list_display = ['Name','AreaId', 'Babyseat','Ostomate','Nursingbed','Washlet','Rotation','Emergencycall']
    search_fields = [ 'Name' ]
    resource_class = ToiletResource
    formats = [base_formats.CSV]
admin.site.register(models.Toilet, ToiletAdmin)

# Hotel import_export
class HotelResource(resources.ModelResource):
    class Meta:
        model = Hotel
class HotelAdmin( geoadmin.OSMGeoAdmin,ImportExportModelAdmin):
    list_display = ['Name','AreaId', 'TEL','Address']
    search_fields = [ 'Name' ]
    resource_class = HotelResource
    formats = [base_formats.CSV]
admin.site.register(models.Hotel, HotelAdmin)

# Hotel
#class HotelAdmin(geoadmin.OSMGeoAdmin):
#    list_display = ['Name','AreaId', 'TEL','Address']
#    search_fields = [ 'Name' ]
#admin.site.register(models.Hotel, HotelAdmin)

# Booklet PDF
class BookletAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Publication', 'PDFfile' ]
    ordering = [ 'Publication' ]
admin.site.register(models.Booklet, BookletAdmin)

