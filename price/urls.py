from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^load_price$', views.load_price, name='load_price'),
    url(r'^search$', views.search_position, name='search_position'),
]