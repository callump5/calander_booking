from django import forms
from .models import Booking,Product


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('day', 'start_time', 'notes', 'type_class', 'stripe_id')

    day = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))

    MONTHS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]

    MONTH_CHOICES = list(enumerate(MONTHS, 1))
    YEAR_CHOICES = [(i, i) for i in range(2016, 2027)]

    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='CVV')
    expiry_month = forms.ChoiceField(choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(choices=YEAR_CHOICES)

    stripe_id = forms.CharField(widget=forms.HiddenInput)


