from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from feedwork.models import *
from feedwork.forms import *
from feedwork.helper_functions import * 
from django.db.models import Q
from django.utils import timezone

from django.http import HttpResponseRedirect

import snoop
@snoop
def index(request):
    
    return render(request,"index.html",{})

def setup_raw_material_names(request):
    context = {}
    # add the dictionary during initialization
    form = raw_material_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
      
            form.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "raw_material_names.html",{'form':form})

def view_raw_material_names(request):
    #get the date from the user 
    # start_date = request.POST.get('start_date')
    # end_date = request.POST.get('end_date')

    # run a query to get all the supplies on that date
    raw_material_names = raw_materials.objects.all()
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_raw_material_names.html", {'raw_material_names':raw_material_names})

def update_raw_material_name(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        # print (pk)
        # clean_pk = pk.strip("/")
        # print (clean_pk)
        raw_material_name_record = raw_materials.objects.get(id=pk)
        form = raw_material_form(request.POST or None, instance=raw_material_name_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_raw_material_names.html",context=context_dict)

def delete_raw_material_name(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        raw_material_name_to_delete = raw_materials.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        raw_material_name_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_raw_material_names/')

def enroll_suppliers(request):
    context = {}
    # add the dictionary during initialization
    form = supplier_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
      
            form.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "suppliers.html",context=context)

def view_suppliers(request):
    # run a query to get all the supplies on that date
    all_suppliers = suppliers.objects.all()
     
    return render(request, "view_suppliers.html", {'all_suppliers':all_suppliers})

def update_suppliers(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        supply_record = suppliers.objects.get(id=clean_pk)
        form = supplier_form(request.POST or None, instance=supply_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_suppliers.html",context=context_dict)

def delete_suppliers(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        supplier_to_delete = suppliers.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        supplier_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_suppliers/')

def enroll_employee(request):
    context = {}
    # add the dictionary during initialization
    form = employee_enrollment_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
      
            form.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "employee_enrollment.html",context=context)

@snoop
def see_employees(request):
    #get the date from the user 
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    # broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

    # run a query to get all the supplies on that date
    employees = employee.objects.filter(date__range=[start_date, end_date])
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_employees.html", {'employees':employees})

def update_employees(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        employee_record = employee.objects.get(id=clean_pk)
        form = employee_enrollment_form(request.POST or None, instance=employee_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_employees.html",context=context_dict)


def make_employee_terms(request):
    context = {}
    # add the dictionary during initialization
    form = employment_terms_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
      
            form.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "employee_terms.html",context=context)

def view_employment_terms(request):
    #get the date from the user 
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    
    terms = employment_terms.objects.filter(date__range=[start_date, end_date])
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_employee_terms.html", {'terms':terms})

def updating_employment_terms(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        employee_term = employment_terms.objects.get(id=clean_pk)
        form = employment_terms_form(request.POST or None, instance=employee_term)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_employment_terms.html",context=context_dict)

def delete_employment_terms(request):
    
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        terms_to_delete = employment_terms.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        terms_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_employee_terms/')

def make_advance(request):
    context = {}
    # add the dictionary during initialization
    form = advance_payment_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
      
            form.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "advance.html",context=context)

def view_advance(request):
    
    #get the date from the user 
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date') 

    # run a query to get all the supplies on that date
    payments = advance_payment.objects.filter(date__range=[start_date, end_date])
     
    terms = employment_terms.objects.filter(date__range=[start_date, end_date])
    return render(request,"view_advance_payments.html",{'payments':payments,'terms':terms})

def update_advance(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        employee_term = advance_payment.objects.get(id=clean_pk)
        form = advance_payment_form(request.POST or None, instance=employee_term)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_advance_payments.html",context=context_dict)


def delete_advance(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        advance_to_delete = advance_payment.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        advance_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_advance_payments/')
