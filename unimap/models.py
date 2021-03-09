####
#   unimap
####
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.gis.db import models as geoModels

# 推奨コース
class Course(models.Model):
    CourseName = models.CharField(verbose_name="コース名",max_length=128)
    CourseAbstruct = models.CharField(verbose_name="概要",max_length=256)
    
    def __str__(self):
        return self.CourseName

    class Meta:
        verbose_name = '推奨ルート'
        verbose_name_plural = '推奨ルート'

class Border(models.Model):
    n03_001 = geoModels.CharField(verbose_name='都道府県名', max_length=10)
    n03_002 = geoModels.CharField(verbose_name='支庁名', max_length=20, blank=True)
    n03_003 = geoModels.CharField(verbose_name='群・政令市名', max_length=20, blank=True)
    n03_004 = geoModels.CharField(verbose_name='市区町村名', max_length=20, blank=True)
    n03_007 = geoModels.CharField(verbose_name='行政区域コード', max_length=5)
    geom    = geoModels.PolygonField(srid=4326)
    objects = geoModels.Manager()
    
    def __str__(self):
        return "%s_%s_%s" % (self.n03_001,self.n03_003,self.n03_004)

    class Meta:
        verbose_name = ('行政区域')
        verbose_name_plural = ('行政区域一覧')
        

