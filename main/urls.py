from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^take/$', views.TakeImages, name="TakeImages"),
    url(r'^train/$', views.TrainImages, name="TrainImages"),
    url(r'^track/$', views.TrackImages, name="TrackImages"),
]