import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Company
from .forms import CompanyForm
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'index.html')

@user_passes_test(lambda u: u.is_superuser)
def company_list(request):
    return render(request, 'company_list.html', {
        'companys': Company.objects.all(),
    })

@user_passes_test(lambda u: u.is_superuser)
def add_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.author=request.user
            company.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "companyListChanged": None,
                        "showMessage": f"{company.name} added."
                    })
                })
    else:
        form = CompanyForm()
    return render(request, 'company_form.html', {
        'form': form,
    })

@user_passes_test(lambda u: u.is_superuser)
def edit_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.author=request.user
            company.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "companyListChanged": None,
                        "showMessage": f"{company.name} updated."
                    })
                }
            )
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company_form.html', {
        'form': form,
        'company': company,
    })

@user_passes_test(lambda u: u.is_superuser)
@ require_POST
def remove_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "companyListChanged": None,
                "showMessage": f"{company.name} deleted."
            })
        })
