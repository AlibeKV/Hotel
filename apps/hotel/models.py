from django.db.models import *


class Hotel(Model):

    title = CharField(verbose_name='имя отеля', max_length=256)
    addres = CharField(verbose_name='адресс', max_length=256)
    city = CharField(verbose_name='город',max_length=256)
    country = CharField(verbose_name='страна',max_length=256)
    rating = DecimalField(verbose_name='рейтинг',max_length=256)


    
    def __str__(self):
        return f'{self.title}'
    
    