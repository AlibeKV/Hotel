from django.db.models import *


class Guest(Model):
    fir_name = CharField(verbose_name='Имя Гостя')
    last_name = CharField(verbose_name='Фамилия ГОстя')
    email = EmailField(verbose_name='email Гостя')
    phone_number = CharField(verbose_name='телефон номер гостя')


    
    def __str__(self):
        return f'{self.fir_name}'
    
    
    