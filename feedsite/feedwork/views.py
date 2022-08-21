from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from feedwork.models import *
import statistics
from feedwork.forms import *
from feedwork.helper_functions import * 
from django.db.models import Q
from django.utils import timezone

from django.http import HttpResponseRedirect
from feedwork.models import *
import snoop
import json
@snoop
def index(request):
    if request.method == 'POST':
        
        selected_date = request.POST.get('start_date')

        # basic_inputs = raw_materials.objects.all()

        # raw_material_stock_balance = {}

        # for basic_input in basic_inputs:

        #     name = basic_input.raw_material_name

        #     raw_material_stock_balance[name] = stock_balance_for_raw_materials(selected_date,basic_input.raw_material_name)

        # #Stock balance for products
        # out_come_names = product_names.objects.all()

        # product_stock_balance = {}

        # for out_come_name in out_come_names:

        #     product_stock_balance[out_come_name.product_name] = stock_balance_for_products(out_come_name.product_name,selected_date)
    

        print("The cost price of raw material is ",cost_price_of_raw_material(selected_date,'maize_bran'))

        # cost price of a particular a product by date

        result_name = product_names.objects.filter(product_name='layers marsh')

        # Find out the raw materials that are involved in that product

        separations = raw_material_separations.objects.filter(product_name__product_name='layers marsh')

        names = {}

        for separation in separations:

            names[separation.separation_name]=separation.raw_material_name.raw_material_name

        # understand to which raw material do those separation names belong

        print(names)


        # Find the cost prices of the different raw materials involved in that product

        cost_price_dict = {}

        for key , value in names.items():

            cost_price_dict[value]=cost_price_of_raw_material(selected_date,value)

        print(cost_price_dict)
        

        #Find the standard weight of the product

        separations = raw_material_separations.objects.filter(product_name__product_name='layers marsh')

        ratios = {}

        standard_weight = 0

        for separation in separations:

            ratios[separation.raw_material_name.raw_material_name]=separation.ratio

        for key, value in ratios.items():

            standard_weight += value

        print(standard_weight)

        print(ratios)

        ## Divide those cost prices by the specific ratios involved in the standard weight of a product

        divided_cost_price_dict = {}

        loop = 0

        for raw_material, cost_price in cost_price_dict.items():

            print(raw_material,"",cost_price)

            if raw_material in ratios.keys():

                print("Yes, it exists and if so then...")

                #divide the cost price of the raw material by the ratio that goes into the standard weight

                divided_cost_price_dict[raw_material]=int(cost_price/ratios[raw_material])

        print(divided_cost_price_dict)

      
        ## Findout the cost prices involved in one kilogram of the product

        standard_cost_price = 0 

        for key , value in divided_cost_price_dict.items():

            standard_cost_price += value

        print(standard_cost_price)

        #How about the cost price of one kilogram of standard weight of a product

        one_kilogram_of_standard_weight = standard_weight/standard_cost_price 

        print(one_kilogram_of_standard_weight)

        # Mulitply that with the quantity of the product that has been sold till a particular date.

        #Get date of the first sale of a particular product

        sale = product_sales.objects.filter(product_name__product_name='layers marsh').first()

        if sale == None:

            pass

        else:

            start_date = sale.date

            #Get amount of the product that had been sold till a particular date

            product_sale_list = []

            sales = product_sales.objects.filter(date__range=[start_date,selected_date])

            for deal in sales:

                product_sale_list.append(deal.quantity)

            total_deals = sum(product_sale_list)

            cost_price = one_kilogram_of_standard_weight * total_deals

            # return cost_price

            
        return render(request,"index.html",{})

    else:
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

def setup_expense_names(request):
    context = {}
    # add the dictionary during initialization
    form = expense_name_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():   
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "expense_names.html",context=context)

def view_expense_names(request):
    #get the date from the user 
    # start_date = request.POST.get('start_date')
    # end_date = request.POST.get('end_date')
    names = expense_names.objects.all()
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_expense_names.html", {'names':names})

def update_expense_names(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        name_record = expense_names.objects.get(id=clean_pk)
        form = expense_name_form(request.POST or None, instance=name_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_expense_names.html",context=context_dict)

def delete_expense_names(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        expense_to_delete = expense_names.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        expense_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_expense_names/')


def setup_expense_units(request):
    context = {}
    # add the dictionary during initialization
    form = expense_unit_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():   
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "expense_units.html",context=context)

def view_expense_units(request):
    #get the date from the user 
    # start_date = request.POST.get('start_date')
    # end_date = request.POST.get('end_date')

    # broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

    # run a query to get all the supplies on that date
    units = expense_units.objects.all()
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_expense_units.html", {'units':units})

def delete_expense_units(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        unit_to_delete = expense_units.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        unit_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_expense_units/')


def update_expense_units(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        expense_record = expense_units.objects.get(id=clean_pk)
        form = expense_unit_form(request.POST or None, instance=expense_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_expense_units.html",context=context_dict)

def record_expenses(request):
    context = {}
    # add the dictionary during initialization
    form = expense_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():   
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "expenses.html",context=context)

def view_expenses(request):
        #get the date from the user 
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    
    costs = expenses.objects.filter(date__range=[start_date, end_date])
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_expenses.html", {'costs':costs})

def update_expenses(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        expense_record = expenses.objects.get(id=clean_pk)
        form = expense_form(request.POST or None, instance=expense_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_expenses.html",context=context_dict)

def delete_expenses(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        expense_to_delete = expenses.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        expense_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_expenses/')

def enroll_employee(request):
    context = {}
    # add the dictionary during initialization
    form = employee_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():   
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "employee.html",context=context)

@snoop
def see_employees(request):
    #get the date from the user 
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    # broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

    # run a query to get all the supplies on that date
    employees = employee.objects.all()
     
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
        form = employee_form(request.POST or None, instance=employee_record)
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
    form = employment_term_form(request.POST or None)
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

    
    terms = employment_terms.objects.all()
     
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
        form = employment_term_form(request.POST or None, instance=employee_term)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_employment_terms.html",context=context_dict)

def deleting_employment_terms(request):
    
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
    payments = advance_payments.objects.filter(date__range=[start_date, end_date])
     
    terms = employment_terms.objects.filter(date__range=[start_date, end_date])
    return render(request,"view_advance_payments.html",{'payments':payments,'terms':terms})

def update_advance(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        employee_term = advance_payments.objects.get(id=clean_pk)
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
        advance_to_delete = advance_payments.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        advance_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_advance_payments/')

def pay_salary(request):
    context = {}
    # add the dictionary during initialization
    form = salary_payment_form(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
      
            form.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form

    return render(request, "salary.html",context=context)


def view_salary(request):
    
    #get the date from the user 
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date') 

    # run a query to get all the supplies on that date
    salaries = salary_payments.objects.filter(date__range=[start_date, end_date])
     
    terms = employment_terms.objects.filter(date__range=[start_date, end_date])
    return render(request,"view_salaries.html",{'salaries':salaries,'terms':terms})

def update_salary(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        payment = salary_payments.objects.get(id=clean_pk)
        form = salary_payment_form(request.POST or None, instance=payment)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 

    return render(request,"update_salaries.html",context=context_dict)


def delete_salary(request):
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        salary_to_delete = salary_payments.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        salary_to_delete.delete()
    
    return HttpResponseRedirect('http://127.0.0.1:8000/view_salaries/')
