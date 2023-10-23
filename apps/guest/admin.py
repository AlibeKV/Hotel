from django.contrib.admin import *

from .models import Guest

@register(Guest)

class GuestAdmin(ModelAdmin):

    list_display = ('id','title')
    list_display_links = ('id','title')