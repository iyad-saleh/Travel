from django.shortcuts import render
from .forms import KedForm
from .models import Ked
# Create your views here.




def index(request):
    if hasattr( request.user  ,'is_MANAGER' ) :
        form = KedForm()
        return render(request, 'ked/index.html',{'form': form})
    return HttpResponse(
        status=403,
        headers={
            'HX-Trigger': json.dumps({

               "kedListChanged": None,
            })
        })


def ked_list(request):
    company = request.user.company
    keds = Ked.objects.filter(company=company)
    return render(request, 'ked/ked_list.html', {
        'keds':keds
    })


def add_ked(request):
    pass



def journal_index(request):
    pass

def journal_list(request):
    pass

