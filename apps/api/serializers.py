from rest_framework.serializers import *

from Boking.models import Booking

from guest.models import Guest

from hotel.models import Hotel

from room.models import Room


class Bookingserializer(ModelSerializer):

    class Meta:

        model = Booking
        fields = '__all__'

class Guestserializer(ModelSerializer):

    class Meta:

        model = Guest
        fields = '__all__'

class Hotelserializer(ModelSerializer):

    class Meta:

        model = Hotel
        fields = '__all__'


class Roomserializer(ModelSerializer):

    class Meta:

        model = Room
        fields = '__all__'



