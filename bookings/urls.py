from django.conf.urls import url

from  .views import  get_index, get_booking_system
urlpatterns = [

    url(r'^$', get_index, name='home'),
    url(r'^new/booking/$', get_booking_system)
]