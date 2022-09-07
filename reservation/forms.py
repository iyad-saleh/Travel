from django import forms
from coin.models import Coin
from .models import Reservation, SubReservation
from django.forms import ModelForm, DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# 'title','reservation_type','Date','PNR','trip','vendor','customer','pay_price','pay_coin','sell_price','sell_coin','status',

class ReservationForm(forms.ModelForm):
    # category= forms.ChoiceField(
    #             choices=[(obj,obj) for obj in EmployeeType.objects.all()] )
    # salary_coin= forms.ChoiceField(
    #             choices=[(obj,obj) for obj in Coin.objects.all()] )

    class Meta:
        model = Reservation
        fields = ['title','reservation_type','Date','PNR','trip','vendor','customer','pay_price','pay_coin','sell_price','sell_coin','status',]
        widgets = {
            'Date': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local'}),
        }
    # #         'name': forms.TextInput(attrs={'class': 'form-control'}),


    # #         'salary': forms.TextInput(attrs={'class': 'form-control'}),

    # #         'phone': forms.TextInput(attrs={'class': 'form-control'}),
    #         'memo': forms.TextInput(attrs={'row': '20'}),



# 'passport','priveat_no1','priveat_no2','pay_price','pay_coin','sell_price','sell_coin',
class SubReservationForm(forms.ModelForm):

    class Meta:
        model = SubReservation
        fields = ['passport','priveat_no1','priveat_no2','pay_price','pay_coin','sell_price','sell_coin',]
        # widgets = {
            # 'category': forms.TextInput(attrs={'class': 'form-control'})}
