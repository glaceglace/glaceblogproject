from django.conf.urls import url
from . import views

app_name = 'app_backend'
urlpatterns = [
	url(r'^backend', views.index, name='index'),
	#url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),#每篇文章的地址
	#url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
	#url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
	]
