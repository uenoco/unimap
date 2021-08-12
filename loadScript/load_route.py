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

# geojson ファイルリスト
geojsonlist = [
    'a_asuka_rt.geojson',
    'a_ikarugaoji_rt.geojson',
    'a_kashihara_rt.geojson',
    'a_kasuga_rt.geojson',
    'a_kitamachi_rt.geojson',
    'a_naramachi_rt.geojson',
##    'a_narapark_rt.geojson',
    'a_nishinokyo_rt.geojson',
    'a_takabatake_rt.geojson'
]

# ModelとGeojsonのマッピング
mapping = {
    'Name'      : 'Name',
    'Summery'   : 'Summery',
    'geom'      : 'LINESTRING',
}

# 実行
def run(verbose=True):
    for file in geojsonlist:
        # ファイルパス
        geojson_file = os.path.abspath(os.path.join(os.path.dirname(__file__), file ))
        print( geojson_file )

        lm = LayerMapping( Route, geojson_file, mapping, transform=False, encoding='UTF-8')
        lm.save( strict=True, verbose=verbose )
    
  
