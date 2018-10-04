from django.shortcuts import render, redirect
from models import Booking

import datetime, calendar

from django.contrib import admin
import datetime
import calendar
from django.core.urlresolvers import reverse
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe

from .forms import BookingForm


# Create your views here.


def get_index(request):
    return render(request, 'index.html')


def get_booking_system(request):


    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})
