####
#   unimap
####
from django.contrib.auth import get_user_model
#from django.db import models
from django.contrib.gis.db import models as models

# 推奨コース
class Area(models.Model):
    Name     = models.CharField(verbose_name="エリア名",max_length=32)
    SubName  = models.CharField(verbose_name="タイトル",max_length=256)
    Abstruct = models.CharField(verbose_name="概要",max_length=256)
    Booklet  = models.CharField(verbose_name="収録冊子",max_length=32)
    Timestamp= models.DateTimeField(verbose_name="更新日時", blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'エリア'
        verbose_name_plural = 'エリア'

# 地点
class PointData(models.Model):
    PointType_CHOICES = ( ( 1, 'route'), ( 2, 'start'), ( 3, 'end'), ( 4, 'start_op'), ( 5, 'end_op'),
                          ( 6, 'location'), ( 7, 'barrguide'), ( 8, 'attension'), ( 9, 'cation'), ( 10, 'busstop') )

    AreaId    = models.ForeignKey('Area', to_field='id', on_delete=models.PROTECT, verbose_name="エリアID")
    Sort      = models.IntegerField(verbose_name="地点タイプ",choices=PointType_CHOICES, null=False)
    No        = models.IntegerField(verbose_name="地点番号")
    Name      = models.CharField(verbose_name="エリア名",max_length=32)
    Summery   = models.CharField(verbose_name="概要",max_length=256)
    Remarks   = models.CharField(verbose_name="備考",max_length=256)
    Open      = models.TimeField(verbose_name="開始時刻")
    Close     = models.TimeField(verbose_name="終了時刻")
    OpeningNote= models.CharField(verbose_name="時刻注釈",max_length=256)
    Holiday   = models.CharField(verbose_name="休日",max_length=256)
    Price     = models.IntegerField(verbose_name="価格")
    PriceNote = models.CharField(verbose_name="価格注釈",max_length=256)
    Discount  = models.CharField(verbose_name="割引",max_length=256)
    Tel       = models.CharField(verbose_name="電話番号",max_length=16)
    Url       = models.CharField(verbose_name="URL",max_length=256)
    UrlTitle  = models.CharField(verbose_name="URL名称",max_length=32)
    Photo1    = models.CharField(verbose_name="Photo1",max_length=256)
    Photo2    = models.CharField(verbose_name="Photo2",max_length=256)
    Photo3    = models.CharField(verbose_name="Photo3",max_length=256)
    Photo360  = models.CharField(verbose_name="Photo360",max_length=256)
    geom      = models.PointField(srid=4326)
    objects   = models.Manager()
    
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = '地点情報'
        verbose_name_plural = '地点情報'

# 行政境界
class Border(models.Model):
    n03_001 = models.CharField(verbose_name='都道府県名', max_length=10)
    n03_002 = models.CharField(verbose_name='支庁名', max_length=20, blank=True)
    n03_003 = models.CharField(verbose_name='群・政令市名', max_length=20, blank=True)
    n03_004 = models.CharField(verbose_name='市区町村名', max_length=20, blank=True)
    n03_007 = models.CharField(verbose_name='行政区域コード', max_length=5)
    geom    = models.PolygonField(srid=4326)
    objects = models.Manager()
    
    def __str__(self):
        return "%s_%s_%s" % (self.n03_001,self.n03_003,self.n03_004)

    class Meta:
        verbose_name = ('行政区域')
        verbose_name_plural = ('行政区域一覧')
        

