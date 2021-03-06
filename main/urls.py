from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^take/$', views.TakeImages, name="TakeImages"),
    url(r'^add_criminal/$', views.add_criminal, name="add_criminal"),
    url(r'^train/$', views.TrainImages, name="TrainImages"),
    url(r'^trackpage/$', views.trackpage, name="trackpage"),
    url(r'^track/$', views.TrackImages, name="TrackImages"),
    url(r'^login/$', views.mylogin,name="mylogin"),
    url(r'^logout/$', views.mylogout, name="mylogout"),
    # url(r'^register/$', views.myregister,name="myregister"),

]
