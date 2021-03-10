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
    list_display = ['Name', 'SubName', 'Abstruct', 'Booklet', 'Timestamp' ]
admin.site.register(models.Area, AreaAdmin)

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
admin.site.register(models.Toilet, geoadmin.OSMGeoAdmin)

# Hotel
admin.site.register(models.Hotel, geoadmin.OSMGeoAdmin)



