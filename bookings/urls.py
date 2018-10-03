from django.conf.urls import url

from  .views import  get_booking_system
urlpatterns = [

    url(r'^$', get_booking_system)
]