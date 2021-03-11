####
#   Unimap Project
####
from django.contrib import admin
from django.contrib.gis import admin as geoadmin 
from . import models

# Register your models here.

#from unimap.models import Border, RecommendCourse
from unimap.models import Area, PointData

# Area
class AreaAdmin(admin.ModelAdmin):
    list_display = ['Name', 'SubName', 'Booklet', 'DEF_LON', 'DEF_LAT' , 'DEF_Zoom' ]
admin.site.register(models.Area, AreaAdmin)

class ImageMapAdmin(admin.ModelAdmin):
    list_display = ['AreaId', 'ImageMap', 'LAT1', 'LON1', 'LAT2', 'LON2' ]
admin.site.register(models.ImageMap, ImageMapAdmin)

# Point
class PointDataAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Sort', 'No', 'Summery', 'geom' ]
admin.site.register(models.PointData, geoadmin.OSMGeoAdmin)

#admin.site.register(models.PointData, geoadmin.OSMGeoAdmin)

# Route
admin.site.register(models.Route, geoadmin.OSMGeoAdmin)

# Slope
admin.site.register(models.Slope, geoadmin.OSMGeoAdmin)

# Zone
admin.site.register(models.Zone, geoadmin.OSMGeoAdmin)

# Toilet
class ToiletAdmin(geoadmin.OSMGeoAdmin):
    list_display = ['AreaId','Name','Summery','Babyseat','Ostomate','Nursingbed','Washlet','Rotation','Emergencycall']
    
admin.site.register(models.Toilet, ToiletAdmin)
# admin.site.register(models.Toilet, geoadmin.OSMGeoAdmin)

# Hotel
admin.site.register(models.Hotel, geoadmin.OSMGeoAdmin)



