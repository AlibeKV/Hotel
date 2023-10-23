from django.contrib.admin import *

from .models import Booking


@register(Booking)

class BookingAdmin(ModelAdmin):
    
    list_display = ('id','title')
    list_display_links = ('id','title')
