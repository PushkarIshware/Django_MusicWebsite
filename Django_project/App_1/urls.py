from django.urls import path
from django.conf.urls import url
from . import views

app_name = "App_1"

urlpatterns = [
    # homepage means 8000/
    url(r'^$', views.index, name='index'),

    # /app1/<album_id>1 or 2 or 3 so on
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),

    # app/<album_id>/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name="favorite")
]
