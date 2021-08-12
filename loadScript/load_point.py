# -*- coding: utf-8 -*-
####
#   Unimap Project load_hotel.py     
####
#   TO RUN this script, Type follows: 
# % cd ..
# % ./manage.py shell                
# >>> from loadScript import load_hotel
# >>> load_hotel.run()
# exstra exec
# >>> import importlib
# >>> importlib.reload( load_hotel )
# >>> load_hotel.run()
####
import os
from django.contrib.gis.utils import LayerMapping
from unimap.models import PointData
#from unimap.models import PointData

# geojson ファイルリスト
geojsonlist = [
    'a_asuka_po.geojson',
    'a_ikarugaoji_po.geojson',
    'a_kashihara_po.geojson',
    'a_kasuga_po.geojson',
    'a_kitamachi_po.geojson',
    'a_naramachi_po.geojson',
##    'a_narapark_po.geojson',
    'a_nishinokyo_po.geojson',
    'a_takabatake_po.geojson'
]

# ModelとGeojsonのマッピング
mapping = {
#   'Sort'      : 'Sort',
#    'No'        : 'No' ,
    'Name'      : 'Name',
    'Summery'   : 'Summery',
    'Remarks'   : 'Remarks',
    'Open'      : 'Open',
    'Close'     : 'Close',
    'OpeningNote': 'OpeningNote',
    'Holiday'   : 'Holiday',
    'Price'     : 'Price',
    'PriceNote' : 'PriceNote',
    'Discount'  : 'Discount',
    'TEL'       : 'TEL' ,
    'URL'       : 'URL' ,
    'Urltitle'  : 'Urltitle',
    'Photo1'    : 'Photo1',
    'Photo2'    : 'Photo2',
    'Photo3'    : 'Photo3',
    'Photo360'  : 'Photo360',
    'Photo360_2': 'Photo360_2',
    'geom'      : 'POINT',
}

# 実行
def run(verbose=True):
    
    for file in geojsonlist:
        # ファイルパス
        geojson_file = os.path.abspath(os.path.join(os.path.dirname(__file__), file ))
        print( geojson_file )

#        lm = LayerMapping( PointData, geojson_file, mapping, transform=False, encoding='UTF-8')
#        lm.save( strict=True, verbose=verbose )

    
  
