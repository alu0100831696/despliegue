from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test/$', views.test, name='test'),
  url(r'^loadRestaurants/$', views.loadRestaurants),
  url(r'^addRestaurants/$', views.addRestaurants, name="addRestaurants"),
  url(r'^delRestaurants/$', views.delRestaurants, name="delRestaurants"),
  url(r'^updateRestaurants/$', views.updateRestaurants, name="updateRestaurants"),

]