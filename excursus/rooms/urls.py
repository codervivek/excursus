from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^category/(?P<slug>[^/]+)/$', views.category),
    url(r'^category/post/(?P<slug>[^/]+)/$', views.post),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post-detail'),
]