from django.conf.urls import url

from  .views import  get_home, get_booking_system
urlpatterns = [

    url(r'^$', get_home, name='home'),
    url(r'^booking/(?P<session_id>\d+)/$', get_booking_system, name='book')
]