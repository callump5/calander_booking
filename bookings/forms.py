from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    # the default format is %Y-%m-%d
    day = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))

    class Meta:
        model = Booking
        fields = ('day', 'start_time', 'session_class', 'notes')