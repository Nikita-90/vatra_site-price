from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^statistics/$', views.statistics_hits, name='statistics_hits'),
]
