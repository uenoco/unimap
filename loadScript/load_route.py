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
from unimap.models import Route

# ファイルパス
geojson_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'a_narapark_rt.geojson'))

# ModelとGeojsonのマッピング
mapping = {
    'Name'      : 'Name',
    'Summery'   : 'Summery',
    'geom'      : 'LINESTRING',
}

# 実行
def run(verbose=True):
    lm = LayerMapping( Route, geojson_file, mapping, transform=False, encoding='UTF-8')
    lm.save( strict=True, verbose=verbose )
    
  
