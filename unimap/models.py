# -*- coding: utf-8 -*-
####
#   Unimap Project models.py     
####
from django.contrib.auth import get_user_model

#from django.db import models
from django.contrib.gis.db import models as models
from django.contrib.gis.geos import Point, LineString

#FileValidator
from django.core.validators import FileExtensionValidator

import os
    
# 推奨コース
class Area(models.Model):
    id       = models.AutoField(primary_key=True)
    DisplayOrder = models.IntegerField(verbose_name="表示順",null=True,blank=True)
    DisplayFlag  = models.BooleanField(verbose_name="表示ON/OFF",default=False)
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
    id       = models.AutoField(primary_key=True)
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
        verbose_name = '2.イラストマップ'
        verbose_name_plural = '2.イラストマップ'
    # See https://qiita.com/kojionilk/items/da20c732642ee7377a78
    
# 移動ルート
class Route(models.Model):
    SortType_CHOICES = ( ( 1, 'メインコース'),( 2, 'オプション'), ( 11, 'ゆるい坂'),( 12, '中くらいの坂'),( 13, '急な坂') )
    id       = models.AutoField(primary_key=True)
    AreaId   = models.ForeignKey('Area', to_field='id', on_delete=models.PROTECT, verbose_name="エリアID", default=1)
    Sort     = models.IntegerField(verbose_name="ルート種類",choices=SortType_CHOICES, default=1 )
    Name     = models.CharField(verbose_name="名称",max_length=24,null=False)
    Summery  = models.CharField(verbose_name="概要",max_length=256,null=True,blank=True)
    geom     = models.LineStringField(verbose_name="ルート座標",srid=4326,default=LineString( [135.82, 34.681],[135.83, 34.685]) )
    Timestamp= models.DateTimeField(verbose_name="更新日時",blank=True, null=True, auto_now=True)

    def _get_linestring(self):
        "Returns a linestring"
        return '%s' % ( self.geom)
    LineString = property(_get_linestring)
    
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = '3.推奨ルート'
        verbose_name_plural = '3.推奨ルート'

# 地点
class PointData(models.Model):
    PointType_CHOICES = ( ( 1, 'route'), (12, 'option' ),
                          ( 2, 'start'), ( 3, 'end'), ( 4, 'start_op'), ( 5, 'end_op'),
                          ( 7, 'barrguide'), ( 14, 'roadguide'),
                          ( 8, 'attention'), ( 9, 'caution'),
                          ( 6, 'location'), (10, 'busstop'),
                          (11, 'shop' ) ,  (13,'restaurant') 
                         )

    id        = models.AutoField(primary_key=True)
    AreaId    = models.ForeignKey('Area', to_field='id', on_delete=models.PROTECT, verbose_name="エリアID", default=1)
    Sort      = models.IntegerField(verbose_name="地点タイプ",choices=PointType_CHOICES, default=1 )
    No        = models.IntegerField(verbose_name="地点番号",null=True,blank=True)
    Name      = models.CharField(verbose_name="エリア名",max_length=24,null=False)
    Summery   = models.CharField(verbose_name="概要",max_length=256,null=True,blank=True)
    Remarks   = models.CharField(verbose_name="備考",max_length=256,null=True,blank=True)
    Open      = models.CharField(verbose_name="開始時刻",max_length=256,null=False,blank=True)
    Close     = models.CharField(verbose_name="終了時刻",max_length=256,null=False,blank=True)
    OpeningNote= models.CharField(verbose_name="時刻注釈",max_length=256,null=False,blank=True)
    Holiday   = models.CharField(verbose_name="休日",max_length=256,null=False,blank=True)
    Price     = models.CharField(verbose_name="価格",max_length=256,null=False,blank=True)
    PriceNote = models.CharField(verbose_name="価格注釈",max_length=256,null=False,blank=True)
    Discount  = models.CharField(verbose_name="割引",max_length=256,null=False,blank=True)
    TEL       = models.CharField(verbose_name="電話番号",max_length=16,null=False,blank=True)
    URL       = models.CharField(verbose_name="URL",max_length=256,null=False,blank=True)
    Urltitle  = models.CharField(verbose_name="URL名称",max_length=24,null=False,blank=True)
    Image1    = models.ImageField(verbose_name="画像１",upload_to="photos/point/",null=True,blank=True)
    Image2    = models.ImageField(verbose_name="画像２",upload_to="photos/point/",null=True,blank=True)
    Photo1    = models.CharField(verbose_name="Photo1",max_length=256,null=True,blank=True)
    Photo2    = models.CharField(verbose_name="Photo2",max_length=256,null=True,blank=True)
    Photo360  = models.CharField(verbose_name="Photo360",max_length=256,null=True,blank=True)
    geom      = models.PointField(srid=4326,default=Point([135.82, 34.68]))
    Timestamp = models.DateTimeField(verbose_name="更新日時",blank=True, null=True, auto_now=True)
    objects   = models.Manager()
    
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = '4.ルート上の地点'
        verbose_name_plural = '4.ルート上の地点'

# ゾーン
class Zone(models.Model):
    SortType_CHOICES = ( ( 1, 'gravel'),( 2, 'difficulty'),( 3, 'impassable'),( 4, 'traffic') )

    id       = models.AutoField(primary_key=True)
    AreaId    = models.ForeignKey('Area', to_field='id', on_delete=models.PROTECT, verbose_name="エリアID", default=1 )
    Sort      = models.IntegerField(verbose_name="ゾーンタイプ",choices=SortType_CHOICES, default=1 )
    Name      = models.CharField(verbose_name="名称",max_length=24,null=False)
    Summery   = models.CharField(verbose_name="概要",max_length=256,null=True)
    Image1    = models.ImageField(verbose_name="画像１",upload_to="photos/zone/",null=True,blank=True)
    Image2    = models.ImageField(verbose_name="画像２",upload_to="photos/zone/",null=True,blank=True)
    Photo1    = models.CharField(verbose_name="Photo1",max_length=256,null=True,blank=True)
    Photo2    = models.CharField(verbose_name="Photo2",max_length=256,null=True,blank=True)
    Photo360  = models.CharField(verbose_name="Photo360",max_length=256,null=True,blank=True)
    geom      = models.PolygonField(srid=4326)
    Timestamp= models.DateTimeField(verbose_name="更新日時",blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = 'A.ゾーン情報'
        verbose_name_plural = 'A.ゾーン情報'

## WIP try Proxy
#class ZoneProxy(Zone):
#    class Meta:
#        proxy = True


# トイレ
class Toilet(models.Model):
    SortType_CHOICES = ( ( 100, 'toilet'),( 999, 'etc') )

    id       = models.AutoField(primary_key=True)
    AreaId    = models.ForeignKey('Area', to_field='id', on_delete=models.PROTECT, verbose_name="エリアID",null=True)
    Sort      = models.IntegerField(verbose_name="地点タイプ",choices=SortType_CHOICES, default=100 )
    Name      = models.CharField(verbose_name="名称",max_length=24,null=False)
    Summery   = models.CharField(verbose_name="概要",max_length=256,null=True,blank=True)
    Floor     = models.CharField(verbose_name="階数",max_length=24,null=True,blank=True)

    Babyseat  = models.BooleanField(verbose_name="ベビーシート",default=False)
    Ostomate  = models.BooleanField(verbose_name="オストメイト",default=False)
    Nursingbed= models.BooleanField(verbose_name="介護ベット",default=False)
    Washlet   = models.BooleanField(verbose_name="ウォシュレット",default=False)
    Rotation  = models.BooleanField(verbose_name="車いす転回",default=False)
    Emergencycall = models.BooleanField(verbose_name="呼出ボタン",default=False)

    Image1    = models.ImageField(verbose_name="画像１",upload_to="photos/toilet/",null=True,blank=True)
    Image2    = models.ImageField(verbose_name="画像２",upload_to="photos/toilet/",null=True,blank=True)
    Photo1    = models.CharField(verbose_name="Photo1",max_length=256,null=True,blank=True)
    Photo2    = models.CharField(verbose_name="Photo2",max_length=256,null=True,blank=True)
    Photo360  = models.CharField(verbose_name="Photo360",max_length=256,null=True,blank=True)
    geom      = models.PointField(srid=4326,default=Point([135.82, 34.68]))
    Timestamp = models.DateTimeField(verbose_name="更新日時",blank=True, null=True, auto_now=True)
    objects   = models.Manager()
    
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name = 'B.トイレ情報'
        verbose_name_plural = 'B.トイレ情報'

# ホテル
class Hotel(models.Model):
    id       = models.AutoField(primary_key=True)
    AreaId    = models.ForeignKey('Area', to_field='id', on_delete=models.PROTECT, verbose_name="エリアID",null=True,blank=True)
    Name      = models.CharField(verbose_name="名称",max_length=24,null=False)
    Summery   = models.CharField(verbose_name="概要",max_length=256,null=True)
    TEL       = models.CharField(verbose_name="電話",max_length=24,null=False, default=0)
    Address   = models.CharField(verbose_name="住所",max_length=256,null=True,blank=True)
    
    Access    = models.CharField(verbose_name="アクセス",max_length=256,null=True,blank=True)
    Parking   = models.CharField(verbose_name="駐車場",max_length=256,null=True,blank=True)
    Staff     = models.CharField(verbose_name="スタッフ補助",max_length=256,null=True,blank=True)
    Moving    = models.CharField(verbose_name="客室への移動",max_length=256,null=True,blank=True)
    Rental    = models.CharField(verbose_name="貸出し備品",max_length=256,null=True,blank=True)
    Bath      = models.CharField(verbose_name="大浴場",max_length=256,null=True,blank=True)
    URL       = models.CharField(verbose_name="ホテルURL",max_length=256,null=True,blank=True)
    Checkin   = models.TimeField(verbose_name="チェックイン",blank=True, null=True)
    Checkout  = models.TimeField(verbose_name="チェックアウト",blank=True, null=True)

    Toilet     = models.CharField(verbose_name="多目的トイレ",max_length=256,null=True,blank=True)
    ToiletFloor= models.CharField(verbose_name="トイレ階数",max_length=16,null=True,blank=True)
    Babyseat   = models.BooleanField(verbose_name="ベビーシート",default=False)
    Ostomate   = models.BooleanField(verbose_name="オストメイト",default=False)
    Nursingbed = models.BooleanField(verbose_name="介護ベット",default=False)
    Washlet    = models.BooleanField(verbose_name="ウォシュレット",default=False)
    Rotation   = models.BooleanField(verbose_name="車いす転回",default=False)
    Emergencycall = models.BooleanField(verbose_name="呼出ボタン",default=False)

    Image1     = models.ImageField(verbose_name="画像１",upload_to="photos/hotel/",null=True,blank=True)
    Image2     = models.ImageField(verbose_name="画像２",upload_to="photos/hotel/",null=True,blank=True)
    ImageBath  = models.ImageField(verbose_name="浴室画像",upload_to="photos/hotel/",null=True,blank=True)
    ImageToilet= models.ImageField(verbose_name="トイレ画像",upload_to="photos/hotel/",null=True,blank=True)

    RoomName  = models.CharField(verbose_name="ルーム名",max_length=256,null=True,blank=True)
    RoomSize  = models.CharField(verbose_name="室内広さ",max_length=256,null=True,blank=True)
    RoomBath  = models.CharField(verbose_name="室内浴室",max_length=256,null=True,blank=True)
    RoomPrice = models.CharField(verbose_name="価格",max_length=256,null=True,blank=True)

    RoomToilet= models.CharField(verbose_name="室内トイレ",max_length=256,null=True,blank=True)
    RoomBabyseat  = models.BooleanField(verbose_name="ベビーシート",default=False)
    RoomOstomate  = models.BooleanField(verbose_name="オストメイト",default=False)
    RoomNursingbed= models.BooleanField(verbose_name="介護ベット",default=False)
    RoomWashlet   = models.BooleanField(verbose_name="ウォシュレット",default=False)
    RoomRotation  = models.BooleanField(verbose_name="車いす転回",default=False)
    RoomEmergencycall = models.BooleanField(verbose_name="呼出ボタン",default=False)
    
    BreakfastPlace = models.CharField(verbose_name="朝食会場",max_length=256,null=True,blank=True)
    BreakfastArrange = models.CharField(verbose_name="食事アレンジ",max_length=256,null=True,blank=True)

    Photo360room  = models.CharField(verbose_name="部屋画像360URL",max_length=256,null=True,blank=True)
    Photo360bath  = models.CharField(verbose_name="浴室画像360URL",max_length=256,null=True,blank=True)
    Photo360toilet= models.CharField(verbose_name="トイレ画像360URL",max_length=256,null=True,blank=True)
    Remarks   = models.CharField(verbose_name="備考",max_length=256,null=True,blank=True)  

    geom      = models.PointField(srid=4326,default=Point([135.82, 34.68]))
    Timestamp = models.DateTimeField(verbose_name="更新日時",blank=True, null=True, auto_now=True)

    objects   = models.Manager()
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = 'C.ホテル情報'
        verbose_name_plural = 'C.ホテル情報'

# 冊子リスト
class Booklet(models.Model):
    id       = models.AutoField(primary_key=True)
    Name     = models.CharField(verbose_name="冊子名",max_length=24)
    SubName  = models.CharField(verbose_name="サブタイトル",max_length=32)
    Publication= models.DateField(verbose_name="発売時期",blank=True, null=True)
    FileSize = models.CharField(verbose_name="PDFサイズ",max_length=24,null=True,blank=True)
    PDFfile  = models.FileField(verbose_name="冊子PDF",upload_to="pdf/",validators=[ FileExtensionValidator(allowed_extensions=['pdf', ]) ])
    Remarks   = models.CharField(verbose_name="備考",max_length=256,null=True,blank=True)  

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'X.冊子リスト'
        verbose_name_plural = 'X.冊子'

