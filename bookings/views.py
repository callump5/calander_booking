from django.shortcuts import render, redirect,reverse
from django.contrib import messages


from django.template.context_processors import csrf
import stripe
import stripe.error

import datetime

from django.conf import settings
from .forms import BookingForm


# Create your views here.


def get_index(request):

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:

                charge = int(form.cleaned_data['session_class'].price * 100)
                customer = stripe.Charge.create(
                    amount= charge,
                    currency="GBP",
                    description=form.cleaned_data['session_class'],
                    card=form.cleaned_data['stripe_id'],
                )
                if customer.paid:
                    form.save()
                else:
                    messages.error(request, "We were unable to take a payment with that card!")
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")

            messages.success(request, 'Thank you for your booking!')
            return redirect('home')
    else:


        form = BookingForm()
    charge = 0
    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE, 'charge': charge}
    args.update(csrf(request))
    return render(request, 'booking.html', args)
