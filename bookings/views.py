from django.shortcuts import render, redirect,reverse
from django.contrib import messages


from django.template.context_processors import csrf
import stripe
import stripe.error

import datetime

from django.conf import settings
from .forms import BookingForm
from .models import Product


# Create your views here.

def get_home(request):
    session = Product.objects.all()
    args = {'session': session}
    return render(request, 'home.html', args)


def get_booking_system(request, session_id):

    session_name = Product.objects.get(id=session_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                charge = int(session_name.price * 100)
                customer = stripe.Charge.create(
                    amount= charge,
                    currency="GBP",
                    description=form.cleaned_data['type_class'],
                    card=form.cleaned_data['stripe_id'],
                )
                if customer.paid:
                    new_form = form.save(False)
                    new_form.type_class = form.cleaned_data['type_class']
                    new_form.save()
                else:
                    messages.error(request, "We were unable to take a payment with that card!")
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")

            messages.success(request, 'Thank you for your booking!')
            return redirect('home')
    else:
        form = BookingForm()
    args = {'form': form, 'session_id': session_id, 'session_name':session_name, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))
    return render(request, 'booking.html', args)
