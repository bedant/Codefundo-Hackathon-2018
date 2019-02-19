from django.conf.urls import url
from . import views as core_views
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
         
         url(r'^home/$', core_views.home, name='home'),
         url(r'^about_us/$', core_views.about_us, name='about_us'),
         url(r'^contact_us/$', core_views.contact_us, name='contact_us'),
		 url(r'^victim/$', core_views.victim, name='victim'),
		 url(r'^volunteer/$', core_views.volunteer, name='volunteer'),
         url(r'^donationbig/$', core_views.donationbig, name='donationbig'),
		 url(r'^bankportal/$', core_views.bankportal, name='bankportal'),
		
]