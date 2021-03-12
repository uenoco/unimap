# -*- coding: utf-8 -*-
####
#   Unimap Project models.py     
####
from django.contrib.auth import get_user_model
#from django.db import models
from django.contrib.gis.db import models as models
from django.contrib.gis.geos import Point, LineString

# 推奨コース
class Area(models.Model):
    Name     = models.CharField(verbose_name="エリア名",max_length=24)
    SubName  = models.CharField(verbose_name="サブタイトル",max_length=24)
    Abstruct = models.TextField(verbose_name="概要",max_length=256)
    Booklet  = models.CharField(verbose_name="収録冊子",max_length=24,null=True,blank=True)
    DEF_LAT  = models.FloatField(verbose_name="中心緯度",default=34.6)
    DEF_LON  = models.FloatField(verbose_name="中心経度",default=135.8)
    DEF_Zoom = models.IntegerField(verbose_name="ズームレベル",default=15 )
    Timestamp= models.DateTimeField(verbose_name="更新日時",blank=True, null=True, auto_now=True)
    
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = '1.マップエリア'
        verbose_name_plural = '1.マップエリア'

# イラスト地図
class ImageMap(models.Model):
    AreaId   = models.ForeignKey('Area', to_field='id', on_delete=models.PROTECT, verbose_name="エリアID")
    ImageMap = models.ImageField(verbose_name="イラスト地図",upload_to="images/",null=True)
    LAT1     = models.FloatField(verbose_name="左上緯度")
    LON1     = models.FloatField(verbose_name="左上経度")
    LAT2     = models.FloatField(verbose_name="右下緯度")
    LON2     = models.FloatField(verbose_name="右下経度")
    Timestamp= models.DateTimeField(verbose_name="更新日時", blank=True, null=True, auto_now=True)

    #def __str__(self):
    #    return self.AreaId

    class Meta:
        verbose_name = '1.イメージマップ'
        verbose_name_plural = '1.イメージマップ'
    # See https://qiita.com/kojionilk/items/da20c732642ee7377a78
    
# 移動ルート
class Route(models.Model):
    SortType_CHOICES = ( ( 1, 'main'),( 2, 'option') )
    AreaId    = models.ForeignKey('Area', to_field='id', on_delete=models.PROTECT, verbose_name="エリアID")
    Sort      = models.IntegerField(verbose_name="ルート種類",choices=SortType_CHOICES, default=1 )
    Name      = models.CharField(verbose_name="名称",max_length=24,null=False)
    Summery   = models.CharField(verbose_name="概要",max_length=256,null=True,blank=True)
    geom      = models.LineStringField(srid=4326,default=LineString( [135.82, 34.681],[135.83, 34.685]) )
    Timestamp= models.DateTimeField(verbose_name="更新日時",blank=True, null=True, auto_now=True)
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = '2.推奨ルート'
        verbose_name_plural = '2.推奨ルート'

# 地点
class PointData(models.Model):
    PointType_CHOICES = ( ( 1, 'route'), ( 2, 'start'), ( 3, 'end'), ( 4, 'start_op'), ( 5, 'end_op'),
                          ( 6, 'location'), ( 7, 'barrguide'), ( 8, 'attension'), ( 9, 'cation'), ( 10, 'busstop') )

    AreaId    = models.ForeignKey('Area', to_field='id', on_delete=models.PROTECT, verbose_name="エリアID")
    Sort      = models.IntegerField(verbose_name="地点タイプ",choices=PointType_CHOICES, null=False)
    No        = models.IntegerField(verbose_name="地点番号",null=True,blank=True)
    Name      = models.CharField(verbose_name="エリア名",max_length=24,null=False)
    Summery   = models.CharField(verbose_name="概要",max_length=256,null=True,blank=True)
    Remarks   = models.CharField(verbose_name="備考",max_length=256,null=True,blank=True)
    Open      = models.TimeField(verbose_name="開始時刻",null=False,blank=True)
    Close     = models.TimeField(verbose_name="終了時刻",null=False,blank=True)
    OpeningNote= models.CharField(verbose_name="時刻注釈",max_length=256,null=False,blank=True)
    Holiday   = models.CharField(verbose_name="休日",max_length=256,null=False,blank=True)
    Price     = models.IntegerField(verbose_name="価格",null=False,blank=True)
    PriceNote = models.CharField(verbose_name="価格注釈",max_length=256,null=False,blank=True)
    Discount  = models.CharField(verbose_name="割引",max_length=256,null=False,blank=True)
    TEL       = models.CharField(verbose_name="電話番号",max_length=16,null=False,blank=True)
    URL       = models.CharField(verbose_name="URL",max_length=256,null=False,blank=True)
    Urltitle  = models.CharField(verbose_name="URL名称",max_length=24,null=False,blank=True)
    Photo1    = models.CharField(verbose_name="Photo1",max_length=256,null=True,blank=True)
    Photo2    = models.CharField(verbose_name="Photo2",max_length=256,null=True,blank=True)
    Photo3    = models.CharField(verbose_name="Photo3",max_length=256,null=True,blank=True)
    Photo360  = models.CharField(verbose_name="Photo360",max_length=256,null=True,blank=True)
    Photo360_2= models.CharField(verbose_name="Photo360_2",max_length=256,null=True,blank=True)
    Timestamp = models.DateTimeField(verbose_name="更新日時",blank=True, null=True, auto_now=True)
    geom      = models.PointField(srid=4326,default=Point([135.82, 34.68]))
    objects   = models.Manager()
    
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = '3.地点情報'
        verbose_name_plural = '3.地点情報'

# ルート補足
class Slope(models.Model):
    SortType_CHOICES = ( ( 1, 'ゆるい坂'),( 2, '中くらいの坂'),( 3, '急な坂') )

    AreaId    = models.ForeignKey('Area', to_field='id', on_delete=models.PROTECT, verbose_name="エリアID")
    Sort      = models.IntegerField(verbose_name="坂タイプ",choices=SortType_CHOICES, default=1 )
    Name      = models.CharField(verbose_name="名称",max_length=24,null=False)
    Summery   = models.CharField(verbose_name="概要",max_length=256,null=True,blank=True)
    geom      = models.LineStringField(srid=4326,default=LineString( [135.82, 34.681],[135.83, 34.680]) )
    Timestamp= models.DateTimeField(verbose_name="更新日時",blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = '4.ルート補足（坂）'
        verbose_name_plural = '4.ルート補足（坂）'

# ゾーン
class Zone(models.Model):
    SortType_CHOICES = ( ( 1, 'gravel'),( 2, 'difficulty'),( 3, 'impassable'),( 4, 'traffic') )

    AreaId    = models.ForeignKey('Area', to_field='id', on_delete=models.PROTECT, verbose_name="エリアID")
    Sort      = models.IntegerField(verbose_name="ゾーンタイプ",choices=SortType_CHOICES, default=1 )
    Name      = models.CharField(verbose_name="名称",max_length=24,null=False)
    Summery   = models.CharField(verbose_name="概要",max_length=256,null=True)
    Photo1    = models.CharField(verbose_name="Photo1",max_length=256,null=True,blank=True)
    Photo2    = models.CharField(verbose_name="Photo2",max_length=256,null=True,blank=True)
    Photo3    = models.CharField(verbose_name="Photo3",max_length=256,null=True,blank=True)
    Photo360  = models.CharField(verbose_name="Photo360",max_length=256,null=True,blank=True)
    Photo360_2= models.CharField(verbose_name="Photo360_2",max_length=256,null=True,blank=True)
    geom      = models.PolygonField(srid=4326)
    Timestamp= models.DateTimeField(verbose_name="更新日時",blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = '5.ゾーン情報'
        verbose_name_plural = '5.ゾーン情報'

# トイレ
class Toilet(models.Model):
    SortType_CHOICES = ( ( 100, 'toilet'),( 999, 'etc') )

    AreaId    = models.ForeignKey('Area', to_field='id', on_delete=models.PROTECT, verbose_name="エリアID",null=True)
    Sort      = models.IntegerField(verbose_name="地点タイプ",choices=SortType_CHOICES, default=100 )
    Name      = models.CharField(verbose_name="名称",max_length=24,null=False)
    Summery   = models.CharField(verbose_name="概要",max_length=256,null=True,blank=True)
    Floor     = models.CharField(verbose_name="回数",max_length=24,null=True,blank=True)

    Babyseat  = models.BooleanField(verbose_name="ベビーシート")
    Ostomate  = models.BooleanField(verbose_name="オストメイト")
    Nursingbed= models.BooleanField(verbose_name="介護ベット")
    Washlet   = models.BooleanField(verbose_name="ウォシュレット")
    Rotation  = models.BooleanField(verbose_name="車いす転回")
    Emergencycall = models.BooleanField(verbose_name="呼出ボタン")
    Photo1    = models.CharField(verbose_name="Photo1",max_length=256,null=True,blank=True)
    Photo2    = models.CharField(verbose_name="Photo2",max_length=256,null=True,blank=True)
    Photo3    = models.CharField(verbose_name="Photo3",max_length=256,null=True,blank=True)
    Photo360  = models.CharField(verbose_name="Photo360",max_length=256,null=True,blank=True)
    Photo360_2= models.CharField(verbose_name="Photo360_2",max_length=256,null=True,blank=True)
    geom      = models.PointField(srid=4326,default=Point([135.82, 34.68]))
    Timestamp = models.DateTimeField(verbose_name="更新日時",blank=True, null=True, auto_now=True)
    objects   = models.Manager()
    
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name = 'A1.トイレ情報'
        verbose_name_plural = 'A1.トイレ情報'

# ホテル
class Hotel(models.Model):
    SortType_CHOICES = ( ( 101, 'hotel'),( 999, 'etc') )

    AreaId    = models.ForeignKey('Area', to_field='id', on_delete=models.PROTECT, verbose_name="エリアID",null=True)
    Sort      = models.IntegerField(verbose_name="地点タイプ",choices=SortType_CHOICES, default=101 )
    Name      = models.CharField(verbose_name="名称",max_length=24,null=False)
    Summery   = models.CharField(verbose_name="概要",max_length=256,null=True)

    TEL       = models.CharField(verbose_name="電話",max_length=24,null=True,blank=True)
    Address   = models.CharField(verbose_name="住所",max_length=256,null=True,blank=True)
    Access    = models.CharField(verbose_name="アクセス",max_length=256,null=True,blank=True)
    URL       = models.CharField(verbose_name="URL",max_length=256,null=True,blank=True)
    URL_f21   = models.CharField(verbose_name="URL_F21",max_length=256,null=True,blank=True)

    Photo1    = models.CharField(verbose_name="Photo1",max_length=256,null=True,blank=True)
    Photo2    = models.CharField(verbose_name="Photo2",max_length=256,null=True,blank=True)
    Photo3    = models.CharField(verbose_name="Photo3",max_length=256,null=True,blank=True)
    Photo360  = models.CharField(verbose_name="Photo360",max_length=256,null=True,blank=True)
    Photo360_2= models.CharField(verbose_name="Photo360_2",max_length=256,null=True,blank=True)
    geom      = models.PointField(srid=4326,default=Point([135.82, 34.68]))
    Timestamp = models.DateTimeField(verbose_name="更新日時",blank=True, null=True, auto_now=True)
    objects   = models.Manager()
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = 'A2.ホテル情報'
        verbose_name_plural = 'A2.ホテル情報'

# Border        
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
