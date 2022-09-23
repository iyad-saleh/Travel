import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Reservation, SubReservation
from .forms import ReservationForm , SubReservationForm
from customer.models import Customer
from ked.models import Ked, Journal
# from django.contrib.auth.decorators import user_passes_test
# is_MANAGER
# is_RESERVATION
# is_ACCOUNTANT
# is_CUSTOMER
# @user_passes_test(lambda u: u.is_superuser)
def index(request):
    if request.user.is_MANAGER or request.user.is_RESERVATION:
        company = request.user.company
        form = ReservationForm()
        form.fields['customer'].queryset = Customer.objects.filter(client=True).filter(company=company)
        form.fields['vendor'].queryset = Customer.objects.filter(supplier=True).filter(company=company)

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
    reservations = Reservation.objects.filter(company=company)
    return render(request, 'reservation/reservation_list.html', {
        'reservations':reservations
    })

# @user_passes_test(lambda u: u.is_superuser)
def add_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.author=request.user
            reservation.company=request.user.company
            # print('request.user.company',request.user.company)
            reservation.save()
            title = ''
            if form.cleaned_data['title']:
                title += form.cleaned_data['title']
            if form.cleaned_data['reservation_type'] :
               title += ' ' + str(form.cleaned_data['reservation_type'])
            ked = Ked.objects.create(title = title, author= request.user, company =request.user.company )
            journal = Journal.objects.create(
                                    ked = ked ,
                                    account_credit =reservation.vendor.account ,
                                    account_dept = reservation.customer.account   ,
                                    dept =   reservation.pay_price ,
                                    credit = reservation.sell_price   ,
                                    coin = reservation.sell_coin   ,
                                    memo = 'no '   ,
                                    author= request.user,
                                    company =request.user.company
                )
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


