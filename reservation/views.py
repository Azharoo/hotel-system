# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Hotel, Reservation

def all_hotels(request):
    all_hotel = '<ul>'
    for hotel in Hotel.objects.all():
        all_hotel += '<li>' + hotel.hotel_name + '</li>'
    all_hotel += '</ul>'
    return HttpResponse(all_hotel)

def hotel_incity(request):
    hotelInCity = '<ul>'
    for hotel in Hotel.objects.all():
        hotelInCity += '<h4>' + hotel.hotel_city + '</h4>'
        hotelInCity += '<ul> <li>' + hotel.hotel_name + '</li> </ul>'
    hotelInCity += '</ul>'
    return HttpResponse(hotelInCity)

def reservation_list(request):
    reservation = '<ol>'
    for name in Reservation.objects.all():
        reservation += '<p> <li>' + name.customer.name + ' - ' + name.hotel.hotel_name + '<br> <b>From :</b> ' + str(name.start_time)[:-6] + ' <b>to : </b> ' + str(name.end_time)[:-6] + '</li> </p>'
    reservation += '</ol>'
    return HttpResponse(reservation)
