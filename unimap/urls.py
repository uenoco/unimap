# -*- coding: utf-8 -*-
####
#   Unimap Project
####
"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings           # add
from django.conf.urls.static import static # add

from unimap import views

admin.site.site_header='奈良ユニバーサル観光マップ管理画面'
admin.site.site_title='奈良ユニバーサル観光マップ管理画面'
admin.site.index_title='ホーム'


urlpatterns = [
    # 管理ページ
    path('admin/', admin.site.urls),

    # rest-API
    path('api/', include('api.urls')),
    
    # トップページ
    path('', views.toppage, name='toppage'),

    # コース一覧ページ
    path('area', views.arealist, name='arealist'),

    # テストページ
    path('test', views.test, name='test'),

    # エリアマップ
    path('map', views.map, name='map'),
    path('map/<int:areaid>', views.map, name='map'),

    # ホテル詳細
    path('hotel/<int:hotelid>', views.hotel, name='hotel'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static('photo/', document_root=settings.MEDIA_ROOT)
urlpatterns += static('photos/', document_root=settings.MEDIA_ROOT+"/photos")
urlpatterns += static('akalstabimage/', document_root=settings.MEDIA_ROOT+"/akalstabimage")

