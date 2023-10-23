from django.contrib.admin import *

from .models import Room

@register(Room)

class RoomAdmin(ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    