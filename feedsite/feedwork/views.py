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

def setup_logistics(request):
    context = {}
    # add the dictionary during initialization
    form = logistic_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
      
            form.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form
        # HttpResponse('A Purchase cant be transported more than once' )

    return render(request, "logistics.html",context=context)

def view_logistics(request):
    #get the date from the user 
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    logistic = logistics.objects.filter(date__range=[start_date, end_date])
     
    return render(request, "view_logistics.html", {'logistic':logistic})

def update_logistics(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        logistic_record = logistics.objects.get(id=clean_pk)
        form = logistic_form(request.POST or None, instance=logistic_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_employees.html",context=context_dict)

def delete_logistics(request):

    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        logistic_to_delete = logistics.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        logistic_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_logistics/')

def execute_purchases(request):
    context = {}
    # add the dictionary during initialization
    form = purchase_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
      
            form.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "purchases.html",context=context)

def see_purchases(request):
    #get the date from the user 
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    purchase = purchases.objects.filter(date__range=[start_date, end_date])
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_purchase.html", {'purchase':purchase})


def update_purchases(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        purchase_record = purchases.objects.get(id=clean_pk)
        form = purchase_form(request.POST or None, instance=purchase_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_purchases.html",context=context_dict)

def delete_purchases(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        purchase_to_delete = purchases.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        purchase_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_purchases/')

def execute_raw_material_transactions(request):
    context = {}
    # add the dictionary during initialization
    form = raw_material_transaction_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
      
            form.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "execute_raw_material_transactions.html",context=context)

@snoop
def view_raw_material_transactions(request):
    #get the date from the user 
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    material_sales = raw_material_transactions.objects.filter(date__range=[start_date, end_date])
     
    # context ={'material_sales': material_sales}

    return render(request, "view_raw_material_transactions.html", {'material_sales':material_sales})

def update_raw_material_transactions(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        transaction_record = raw_material_transactions.objects.get(id=clean_pk)
        form = raw_material_transactions_form(request.POST or None, instance=transaction_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_raw_material_transactions.html",context=context_dict)

def delete_raw_material_transactions(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        transaction_to_delete = raw_material_transactions.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        transaction_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_raw_material_transactions/')

def setup_product_names(request):
    context = {}
    # add the dictionary during initialization
    form = product_name_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():   
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "setup_product_names.html",context=context)

def view_product_names(request):
    #get the date from the user 
    # start_date = request.POST.get('start_date')
    # end_date = request.POST.get('end_date')

    names = product_names.objects.all()
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_product_names.html", {'names':names})

def update_product_names(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        name_record = product_names.objects.get(id=clean_pk)
        form = product_name_form(request.POST or None, instance=name_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_product_names.html",context=context_dict)    

def delete_product_names(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        name_to_delete = product_names.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        name_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_product_names/')

def setup_products(request):
    context = {}
    # add the dictionary during initialization
    form = product_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():   
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "products.html",context=context)

def view_products(request):
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    
    product = products.objects.filter(date__range=[start_date, end_date])
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_products.html", {'product':product})

def update_products(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        product_record = products.objects.get(id=clean_pk)
        form = product_form(request.POST or None, instance=product_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_products.html",context=context_dict)

def delete_products(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        product_to_delete = products.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        product_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_products/')    


def setup_raw_material_separations(request):
    context = {}
    # add the dictionary during initialization
    form = raw_material_separation_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():   
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "raw_material_separations.html",context=context)

def view_raw_material_separations(request):
    #get the date from the user 
    # start_date = request.POST.get('start_date')
    # end_date = request.POST.get('end_date')    
    seperations = raw_material_separations.objects.all()
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_raw_material_separations.html", {'seperations':seperations})

def update_raw_material_separations(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        separation_record = raw_material_separations.objects.get(id=clean_pk)
        form = raw_material_separation_form(request.POST or None, instance=separation_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_raw_material_separations.html",context=context_dict)   
     
def delete_raw_material_separations(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        separation_to_delete = raw_material_separations.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        separation_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_raw_material_separations/') 

def execute_product_sales(request):
    context = {}
    # add the dictionary during initialization
    form = product_sale_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():   
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "execute_product_sales.html",context=context)

def view_product_sales(request):
    #get the date from the user 
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    # broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

    # run a query to get all the supplies on that date
    sales = product_sales.objects.filter(date__range=[start_date, end_date])
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_product_sales.html", {'sales':sales})

def update_product_sales(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        sale_record = product_sales.objects.get(id=clean_pk)
        form = product_sale_form(request.POST or None, instance=sale_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_product_sales.html",context=context_dict)

def delete_product_sales(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        sale_to_delete = product_sales.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        sale_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_product_sales/')
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
