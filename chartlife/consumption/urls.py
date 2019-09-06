# demo/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^index2', views.index2, name="index2"),
    url(r'^radar/$', views.radar, name="radar"),
]