from __future__ import absolute_import

from django.contrib import admin

from .models import GeoLocation

class GeoLocationModelAdmin(admin.ModelAdmin):
    list_display = ['address', 'lat', 'lng']
    search_fields = ('address', 'lat', 'lng',)

    class Meta:
        model = GeoLocation
admin.site.register(GeoLocation, GeoLocationModelAdmin)
