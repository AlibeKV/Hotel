from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from rest_framework.viewsets import ModelViewSet

from .serializers import Bookingserializer , Guestserializer , Hotelserializer , Roomserializer 

from apps.Boking.models import Booking
from apps.guest.models import Guest
from apps.hotel.models import Hotel
from apps.room.models import Room


from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication



class BookingSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = Bookingserializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class GuestSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = Guestserializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class HotelSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = Hotelserializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class RoomSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = Roomserializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

