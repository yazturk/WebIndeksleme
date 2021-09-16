from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('frekans', views.frekans, name='frekans'),
    path('anahtar', views.anahtar, name='anahtar'),
    path('benzerlik', views.benzerlik, name='benzerlik'),
    path('indeksleme', views.indeksleme, name='indeksleme'),
    path('semantik', views.semantik, name='semantik'),
#   path('anasayfa', views.get_name, name='anasayfa'),
    path('frekans/sonuclar', views.frekans_s, name='frekans_s'),
    path('anahtar/sonuclar', views.anahtar_s, name='anahtar_s'),
    path('benzerlik/sonuclar', views.benzerlik_s, name='benzerlik_s'),
    path('indeksleme/sonuclar', views.indeksleme_s, name='indeksleme_s'),
    path('semantik/sonuclar', views.semantik_s, name='semantik_s'),
]
