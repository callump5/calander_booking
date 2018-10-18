from django.db import models
from django.core.exceptions import ValidationError
from datetime import time

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    slots = models.IntegerField()

    def __unicode__(self):
        return self.name

class Booking(models.Model):

    TIME_CHOICES = (
        (time(11, 00, 00), u'11 AM'),
        (time(12, 00, 00), u'12 PM'),
        (time(13, 00, 00), u'1 PM'),
        (time(14, 00, 00), u'2 PM'),
        (time(15, 00, 00), u'3 PM'),
        (time(16, 00, 00), u'4 PM'),
        (time(17, 00, 00), u'5 PM'),
    )


    day = models.DateField(u'Booking date')


    start_time = models.TimeField(u'Booking time', choices=TIME_CHOICES, max_length=200)
    notes = models.CharField(u'Notes', blank=True, null=True, max_length=500)

    type_class = models.ForeignKey(Product)

    stripe_id = models.CharField(max_length=40, default='')

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking'

    def __unicode__(self):
        return str(self.day) + ' - ' + str(self.start_time)


    def check_availability(self, taken_slots, max_slots):

        full = False

        if taken_slots >= max_slots:
            full = True

        return full


    def clean(self):

        events = Booking.objects.filter(day=self.day, start_time=self.start_time, type_class=self.type_class).count()

        if events:
            if self.check_availability(events, self.type_class.slots):
                raise ValidationError('Too many bookings')
