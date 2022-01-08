from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from feedwork.models import *
from feedwork.forms import *
from feedwork.helper_functions import * 
from django.http import HttpResponseRedirect


def index(request):
    # return HttpResponse("Hello, world. You're at the STS Poultry Business ")
    return render(request, "index.html",{})

def supplying(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    form = SupplyForm(request.POST or None)
    if request.method == 'POST':
        # add the dictionary during initialization

        if form.is_valid():
            form.save()
            #Its here that after the supply is made then we shall start populating the RawMaterialQuantities
            #table
            # we shall check if the "RawMaterialQuantities" table has atleast one row
            compute_quantities()
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        context['form'] = form
       
    return render(request, "supply.html",context)

def viewing_supplies(request):
    #get the date from the user 
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # run a query to get all the supplies on that date
    supplies = RawMaterial.objects.filter(date__range=[start_date, end_date])

    print(type(supplies))
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_supplies.html", {'supplies':supplies})


