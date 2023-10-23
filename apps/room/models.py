from django.db.models import *

from hotel.models import Hotel

class Room(Model):
    hotel = ManyToManyField(Hotel)
    number = IntegerField(verbose_name='номер комнаты')
    capacity = IntegerField(verbose_name='этаж')
    price = IntegerField(verbose_name='цена')


    
    def __str__(self):
        return f'{self.hotel}'
    
