from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import BookingForm


# Create your views here.


def get_index(request):

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Thank you for your booking!')
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'index.html', {'form': form})
