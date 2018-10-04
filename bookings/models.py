from django.db import models
from django.core.exceptions import ValidationError
from datetime import time

# Create your models here.


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


    day = models.DateField(u'Day of booking', help_text='Day of booking')


    start_time = models.TimeField(u'Booking slot', help_text='Booking slot', choices=TIME_CHOICES, max_length=200)
    end_time = models.TimeField(u'Finish time', help_text='Finish Time', choices=TIME_CHOICES, max_length=200)
    notes = models.TextField(u'Notes', help_text='Notes', blank=True, null=True)


    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking'

    def __unicode__(self):
        return str(self.day) + ' - ' + str(self.start_time)


    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end: # Edge case
            overlap = False
        elif new_start == fixed_start or new_end == fixed_end:
            overlap = True
        elif(new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #Inner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: # Outer limits
            overlap = True

        return overlap

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending must be after start time!')

        events = Booking.objects.filter(day=self.day)

        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError('There is an overlap with another booking!: ' + str(event.day)
                                          + ' ' + str(event.start_time) + ' - ' + str(event.end_time))