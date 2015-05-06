# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^book/isbn/$', views.fetch),
    url(r'^book/detail/$', views.upload),
]
