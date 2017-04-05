from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('price.urls')),
    url(r'^vatra/', include('sitevatra.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^resume/', include('pageresume.urls'))
]
