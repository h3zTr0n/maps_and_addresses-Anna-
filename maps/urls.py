""" mysite URL Configuration """
from __future__ import absolute_import
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    url(r'^addresses/', include('addresses.urls')),
    url(r'^admin/', admin.site.urls)
]
