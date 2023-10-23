from django.urls import path , include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

from .views import BookingSet , GuestSet , HotelSet , RoomSet

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view())
]

router = DefaultRouter()
router.register('booking',BookingSet, basename='Booking')
router.register('guest', GuestSet, basename='Guest')
router.register('hotel', HotelSet, basename='Hotel')
router.register('room',RoomSet, basename='room')

urlpatterns += router.urls

