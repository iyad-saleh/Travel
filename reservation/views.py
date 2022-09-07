import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Reservation, SubReservation
from .forms import ReservationForm , SubReservationForm
# from django.contrib.auth.decorators import user_passes_test
# is_MANAGER
# is_RESERVATION
# is_ACCOUNTANT
# is_CUSTOMER
# @user_passes_test(lambda u: u.is_superuser)
def index(request):
    if request.user.is_MANAGER or request.user.is_RESERVATION:
        form = ReservationForm()
        return render(request, 'reservation/index.html',{'form': form,})
    return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "reservationListChanged": None,
            })
        })

# @user_passes_test(lambda u: u.is_superuser)
def reservation_list(request):
    company = request.user.company
    emps = Reservation.objects.filter(company=company)
    return render(request, 'reservation/reservation_list.html', {
        'reservations':emps
    })

# @user_passes_test(lambda u: u.is_superuser)
def add_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.author=request.user
            reservation.company=request.user.company
            print('request.user.company',request.user.company)
            reservation.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "reservationListChanged": None,
                        "showMessage": f"{reservation.title} added."
                    })
                })
    else:
        form = ReservationForm()
    return render(request, 'reservation/reservation_form.html', {
        'form': form,
    })

# @user_passes_test(lambda u: u.is_superuser)
def edit_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.author=request.user

            reservation.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "reservationListChanged": None,
                        "showMessage": f"{reservation.title} updated."
                    })
                }
            )
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservation/reservation_form.html', {
        'form': form,
        'reservation': reservation,
    })

# @user_passes_test(lambda u: u.is_superuser)
@ require_POST
def remove_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "reservationListChanged": None,
                "showMessage": f"{reservation.title} deleted."
            })
        })


