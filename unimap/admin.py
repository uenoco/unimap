####
#   Unimap Project
####
from django.contrib import admin
from django.contrib.gis import admin as geoadmin 
from . import models

# Register your models here.

#from unimap.models import Border, RecommendCourse
from unimap.models import Area, PointData

# Border
#class BorderAdmin(admin.ModelAdmin):
#    list_display = [ "n03_001", "n03_002", "n03_003", "n03_004", "n03_007", "geom"]
#admin.site.register(models.Border, BorderAdmin)
admin.site.register(models.Border, geoadmin.OSMGeoAdmin)

# Area
class AreaAdmin(admin.ModelAdmin):
    list_display = ['Name', 'SubName', 'Abstruct', 'Booklet', 'Timestamp' ]
admin.site.register(models.Area, AreaAdmin)

# Point
class PointDataAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Sort', 'No', 'Summery', 'geom' ]
admin.site.register(models.PointData, geoadmin.OSMGeoAdmin)

#admin.site.register(models.PointData, geoadmin.OSMGeoAdmin)

