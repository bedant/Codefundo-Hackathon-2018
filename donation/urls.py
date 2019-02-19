from django.conf.urls import url
from . import views as core_views
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
         url(r'^admin/', admin.site.urls),
         url(r'^donatorlist/$', core_views.donator_list, name='donatorlist'),
]