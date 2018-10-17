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

    session_name = Session.objects.get(id=session_name)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.session_class = form.cleaned_data['type_class']
            try:
                charge = int(session_name.price * 100)
                customer = stripe.Charge.create(
                    amount= charge,
                    currency="GBP",
                    description=form.cleaned_data['type_class'],
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

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE, 'session_name': session_name}
    args.update(csrf(request))
    return render(request, 'booking.html', args)
