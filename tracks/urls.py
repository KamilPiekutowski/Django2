from django.conf.urls import url
from . import views

app_name = 'tracks'

urlpatterns = [
    # /tracks/
    url(r'^$', views.index, name='index'),

    # /tracks/<album_id>
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /tracks/<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]