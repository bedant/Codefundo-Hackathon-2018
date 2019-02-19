from django.conf.urls import url,include
from django.contrib import admin

from . import views

urlpatterns = [
  url(r'^$', views.helpindex, name='help_index'),
]

urlpatterns+= [   
    url(r'new/$', views.new_help_request, name='new_help_request'),
]