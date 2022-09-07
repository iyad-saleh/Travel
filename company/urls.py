from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='company_index'),
    path('companys/', company_list, name='company_list'),
    path('companys/add', add_company, name='add_company'),
    path('companys/<int:pk>/remove', remove_company, name='remove_company'),
    path('companys/<int:pk>/edit', edit_company, name='edit_company'),
]
