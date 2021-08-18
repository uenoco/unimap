# -*- coding: utf-8 -*-
####
#   Unimap Project load_toilet.py     
####
#   TO RUN this script
#     replace "y" to 1 and "n" to 0 in toilet.geojson
#     and type follows: 
# % cd ..
# % ./manage.py shell                
# >>> from loadScript import load_zone
# >>> load_load_zone.run()
# exstra exec
# >>> import importlib
# >>> importlib.reload( load_toilet )
# >>> load_toilet.run()
####
import os
from django.contrib.gis.utils import LayerMapping
from unimap.models import Zone

# ファイルパス
geojson_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'pass.geojson'))

# ModelとGeojsonのマッピング
##  SortType_CHOICES = ( ( 1, 'gravel'),( 2, 'difficulty'),( 3, 'impassable'),( 4, 'traffic') )
mapping = {
    'Name'      : 'Name',
    'Summery'   : 'Summery',
    'Photo1'    : 'Photo1',
    'Photo2'    : 'Photo2',
    'Photo3'    : 'Photo3',
    'Photo360'  : 'Photo360',
    'Photo360_2': 'Photo360_2',
    'geom' : 'POLYGON',
}

# 実行
def run(verbose=True):
    lm = LayerMapping( Zone, geojson_file, mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
  
