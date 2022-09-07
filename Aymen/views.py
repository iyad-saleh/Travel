from django.shortcuts import render




def dashboard(request):
    # if request.user.is_MANAGER:
    return render(request, 'dashboard.html')