from django.conf.urls import url
from . import views

app_name = 'app_comments'
urlpatterns = [
url(r'^post/(?P<post_pk>[0-9]+)/comment/$', views.post_comment, name='post_comment'),
]