# -*- coding: utf-8 -*-
####
#   Unimap Project load_toilet.py     
####
#   TO RUN this script
#     replace "y" to 1 and "n" to 0 in toilet.geojson
#     and type follows: 
# % cd ..
# % ./manage.py shell                
# >>> from loadScript import load_toilet
# >>> load_toilet.run()
# exstra exec
# >>> import importlib
# >>> importlib.reload( load_toilet )
# >>> load_toilet.run()
####
import os
from django.contrib.gis.utils import LayerMapping
from unimap.models import Toilet

# ファイルパス
geojson_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'toilet.geojson'))

def yn_check( var ):
    if var == 'y':
        return 1
    else:
        return 0

# ModelとGeojsonのマッピング
mapping = {
    'Name'      : 'Name',
    'Summery'   : 'Summery',
    'Floor'     : 'Floor',
    'Photo1'    : 'Photo1',
    'Photo2'    : 'Photo2',
    'Photo3'    : 'Photo3',
    'Photo360'  : 'Photo360',
    'Photo360_2': 'Photo360_2',
    'Babyseat'  : 'babyseat',
    'Ostomate'  : 'ostomate',
    'Nursingbed': 'nursingbed',
    'Washlet'   : 'washlet',
    'Rotation'  : 'rotation',
    'Emergencycall':'emergencycall',
    'geom'      : 'POINT',
}

# 実行
def run(verbose=True):
    lm = LayerMapping( Toilet, geojson_file, mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
  
