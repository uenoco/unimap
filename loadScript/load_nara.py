# -*- coding: utf-8 -*-
####
#   Unimap Project
####
import os
from django.contrib.gis.utils import LayerMapping
from unimap.models import Border

# ModelとGeojsonのマッピング
mapping = {
    'n03_001' : 'N03_001',
    'n03_002' : 'N03_002',
    'n03_003' : 'N03_003',
    'n03_004' : 'N03_004',
    'n03_007' : 'N03_007',
    'geom' : 'POLYGON',
}

# ファイルパス
geojson_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'N03-20_29_200101.geojson'))

# 実行
def run(verbose=True):
    lm = LayerMapping(Border, geojson_file, mapping, transform=False, encoding='UTF-8')
    print( lm )
#    lm.save(strict=True, verbose=verbose)
    
    
