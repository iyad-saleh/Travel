from django.urls import path

from .views import *


urlpatterns = [
    path('', index,name='reservation_index'),
    path('reservations/', reservation_list, name='reservation_list'),
    path('reservations/add', add_reservation, name='add_reservation'),
    path('reservations/<int:pk>/remove', remove_reservation, name='remove_reservation'),
    path('reservations/<int:pk>/edit', edit_reservation, name='edit_reservation'),
    # path('empType/', indexType,  name='indexType'),
    # path('empTypes/', reservation_Type_list, name='reservation_Type_list'),
    # path('empType/add', add_reservation_Type, name='add_reservation_Type'),
    # path('empType/<int:pk>/remove', remove_reservation_Type, name='remove_reservation_Type'),
    # path('empType/<int:pk>/edit', edit_reservation_Type, name='edit_reservation_Type'),
]
