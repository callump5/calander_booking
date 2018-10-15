from django.shortcuts import render, redirect,reverse
from django.contrib import messages


from django.template.context_processors import csrf
import stripe
import stripe.error

import datetime

from django.conf import settings
from .forms import BookingForm
from .models import Session


# Create your views here.

def get_home(request):
    session = Session.objects.all()
    args = {'session': session}
    return render(request, 'home.html', args)


def get_booking_system(request, session_name):
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
                    session = Session.objects.get(id=session_name)
                    new_form = form.save(commit=False)
                    new_form.session_type = session
                    new_form.save()
                else:
                    messages.error(request, "We were unable to take a payment with that card!")
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")

            messages.success(request, 'Thank you for your booking!')
            return redirect('home')
    else:
        form = BookingForm()
    session_name = Session.objects.get(id=session_name)
    charge = 0
    args = {'form': form, 'session_name': session_name, 'publishable': settings.STRIPE_PUBLISHABLE, 'charge': charge}
    args.update(csrf(request))
    return render(request, 'booking.html', args)
