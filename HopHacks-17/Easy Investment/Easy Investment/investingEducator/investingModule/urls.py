from django.conf.urls import url

from investingModule import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
url(r'^test$', views.test, name='test'),
url(r'^userDetails$', views.userDetails, name='userDetails'),
url(r'^landingPage$', views.landingPage, name='landingPage'),
url(r'^stockDetails$', views.stockDetails, name='stockDetails'),
]