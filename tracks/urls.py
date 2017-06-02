from django.conf.urls import url
from . import views

urlpatterns = [
    # /tracks/
    url(r'^$', views.index, name='index'),

    # /tracks/71
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]