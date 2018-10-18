import datetime as dt
from django import template
from django.urls import reverse


from ..models import Product, Booking

register = template.Library()



@register.filter()
def check_slots(sub):
    count = Booking.objects.all().count() * sub
    return count

