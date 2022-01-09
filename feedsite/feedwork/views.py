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

def updating_supplies(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        supply_record = RawMaterial.objects.get(id=clean_pk)
        form = RawMaterialForm(request.POST or None, instance=supply_record)
        if request.method == 'POST':
            if form.is_valid():
                increase_quantity_value = form.cleaned_data['increase_quantity']

                reduce_quantity_value = form.cleaned_data['reduce_quantity']
                
                form.save()
                update_quantites(increase_quantity_value,reduce_quantity_value , form)
                return HttpResponseRedirect('http://127.0.0.1:8000/view_supplies')

        else:
            context_dict["form"] = form
    return render(request,"update_supply.html",context=context_dict)

def deleting_supplies(request):
    # book= get_object_or_404(Book, pk=pk)  
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        supply_record_to_delete = RawMaterial.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        supply_item = supply_record_to_delete.item
        supply_quantity = supply_record_to_delete.quantity
        #put them inside a function right away
        reduce_due_to_deletion(supply_item,supply_quantity) 
        
        supply_record_to_delete.delete()
        # redirect('view_supply.html')
        return HttpResponseRedirect('http://127.0.0.1:8000/view_supplies')
        # if request.method =='POST':
        #   #we get to know the item 

        #     supply_record_to_delete.delete()
        #     return redirect('view_supply.html')

        # context_dict["object"] = supply_record_to_delete
    return render(request, "delete_supply.html",context=context_dict)


