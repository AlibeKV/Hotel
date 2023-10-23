from django.db.models import *


from room.models import Room
from guest.models import Guest


class Booking(Model):
    room = ManyToManyField(Room)
    guest = ManyToManyField(Guest)
    checkin_data = DateField(blank=True,null=True)
    is_paid = BooleanField(verbose_name='Оплата')


    def __str__(self):
        return f'{self.checkin_data}'


