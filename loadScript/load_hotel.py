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
from unimap.models import Hotel

# ファイルパス
geojson_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'hotel.geojson'))

# ModelとGeojsonのマッピング
mapping = {
    'Name'      : 'Name',
    'Summery'   : 'Summery',
    'TEL'       : 'TEL',
    'Address'   : 'Address',
    'Access'    : 'Access',
    'URL'       : 'URL' ,
    'URL_f21'   : 'URL_f21',
    'Photo1'    : 'Photo1',
    'Photo2'    : 'Photo2',
    'Photo3'    : 'Photo3',
    'Photo360'  : 'Photo360',
    'Photo360_2': 'Photo360_2',
    'geom'      : 'POINT',
}

# 実行
def run(verbose=True):
    lm = LayerMapping( Hotel, geojson_file, mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
    
  
