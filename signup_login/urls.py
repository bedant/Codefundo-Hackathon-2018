from django.conf.urls import url
from . import views as core_views
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
         url(r'^login/$', auth_views.login, name='login'),
         #url(r'^logout/$', auth_views.logout, name='logout'),
         url(r'^admin/', admin.site.urls),
         url(r'^signup/$', core_views.signup, name='signup'),
         url(r'^logout/$', auth_views.logout,{'next_page': 'home'},name='logout')
]