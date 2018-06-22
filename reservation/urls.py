from django.conf.urls import url
from .views import all_hotels, hotel_incity, reservation_list

urlpatterns = [
    url(r'hotels', all_hotels),
    url(r'hotelincity', hotel_incity),
    url(r'reservationlist', reservation_list),

]