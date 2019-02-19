
from django.conf.urls import url,include
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^webapp/', include('webapp.urls')),
    url(r'^$',views.index , name='index'),

]
