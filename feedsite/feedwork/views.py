from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from feedwork.models import *
from feedwork.forms import *
from feedwork.helper_functions import * 
from django.http import HttpResponseRedirect


def index(request):
    check_if_raw_material_quantities_are_empty()
    # return HttpResponse("Hello, world. You're at the STS Poultry Business ")
    #To create a new instance of the RMQ model 
    #grab the lastest instance inside the RMQ model
    last_raw_material_qty_occurance = RawMaterialQuantities.objects.last()
    #check if it has any instances , if not then just skip to the end
    count_quantities = RawMaterialQuantities.objects.count()
    if(count_quantities != 0):
        #change dates into some specific dates (%x-Local version of date-12/31/18)
        last_date = last_raw_material_qty_occurance.date
        rear_date = last_date.strftime("%x")
        current_date = datetime.datetime.now()
        earlist_date = current_date.strftime("%x")
        if rear_date == earlist_date:
            print("Dates are equal")
        else:
            #duplicate the last instance
            dup_maize_bran = last_raw_material_qty_occurance.maize_bran 
            dup_cotton = last_raw_material_qty_occurance.cotton
            dup_sun_flower = last_raw_material_qty_occurance.sun_flower
            dup_fish = last_raw_material_qty_occurance.fish
            
            dup_general_purpose_premix = last_raw_material_qty_occurance.general_purpose_premix
            dup_layers_premix = last_raw_material_qty_occurance.layers_premix
            dup_shells = last_raw_material_qty_occurance.shells
            dup_meat_boaster = last_raw_material_qty_occurance.meat_boaster
            dup_egg_boaster=last_raw_material_qty_occurance.egg_boaster
            dup_calcium = last_raw_material_qty_occurance.calcium
            dup_soya_bean = last_raw_material_qty_occurance.soya_bean
            dup_brown_salt = last_raw_material_qty_occurance.brown_salt
            dup_animal_salt = last_raw_material_qty_occurance.animal_salt
            dup_common_salt = last_raw_material_qty_occurance.common_salt 
            dup_coconut = last_raw_material_qty_occurance.coconut 
            dup_pig_concentrate = last_raw_material_qty_occurance.pig_concentrate
            dup_wonder_pig = last_raw_material_qty_occurance.wonder_pig 
            dup_big_pig = last_raw_material_qty_occurance.big_pig 


            duplicate_quantiites = RawMaterialQuantities.objects.create(date = datetime.datetime.now()
                                                                   ,maize_bran = dup_maize_bran 
                                                                   ,cotton = dup_cotton
                                                                   ,sun_flower = dup_sun_flower 
                                                                   ,fish = dup_fish
                                                                   
                                                                   ,general_purpose_premix = dup_general_purpose_premix
                                                                   ,layers_premix = dup_layers_premix
                                                                   ,shells = dup_shells
                                                                   ,meat_boaster = dup_meat_boaster
                                                                   ,egg_boaster=dup_egg_boaster
                                                                   ,calcium = dup_calcium
                                                                   ,soya_bean = dup_soya_bean
                                                                   ,brown_salt = dup_brown_salt
                                                                   ,animal_salt = dup_animal_salt
                                                                   ,common_salt = dup_common_salt
                                                                   ,coconut = dup_coconut
                                                                   ,pig_concentrate = dup_pig_concentrate
                                                                   ,wonder_pig = dup_wonder_pig
                                                                   ,big_pig = dup_big_pig) 
    else:
        print("Just continue with life")

    #do the same with Product 
    lastproduct = ProductQuantities.objects.last()

    count_pq = ProductQuantities.objects.count()
    if(count_pq != 0):
        last_date = lastproduct.date
        rear_date = last_date.strftime("%x")
        current_date = datetime.datetime.now()
        earlist_date = current_date.strftime("%x")
        if rear_date == earlist_date:
            print("Dates are equal")
        else:
            dup_broilers_marsh = lastproduct.broilers_marsh
            dup_chick_marsh = lastproduct.chick_marsh
            dup_old_pig = lastproduct.old_pig
            dup_growers_marsh = lastproduct.growers_marsh
            dup_layers_marsh = lastproduct.layers_marsh
            dup_young_pig = lastproduct.young_pig

            duplicate_quantiites = ProductQuantities.objects.create(date = datetime.datetime.now(),broilers_marsh = dup_broilers_marsh , chick_marsh = dup_chick_marsh , 
                                    old_pig = dup_old_pig , growers_marsh = dup_growers_marsh,layers_marsh = dup_layers_marsh , young_pig = dup_young_pig)
    else:
        print("Just continue with life")

    last_product_price = ProductPrices.objects.last()

    count_pp = ProductPrices.objects.count()
    if(count_pp != 0 ):
        last_date = last_product_price.date
        rear_date = last_date.strftime("%x")
        current_date = datetime.datetime.now()
        earlist_date = datetime.datetime.now()
        earlist_date = current_date.strftime("%x")
        if rear_date == earlist_date:
            print("Dates are equal")
        else:
            dup_broilers_marsh = last_product_price.broilers_marsh
            dup_chick_marsh = last_product_price.chick_marsh
            dup_old_pig = last_product_price.old_pig
            dup_growers_marsh = last_product_price.growers_marsh
            dup_layers_marsh = last_product_price.layers_marsh
            dup_young_pig = last_product_price.young_pig

            duplicate_prices = ProductQuantities.objects.create(date = datetime.datetime.now(),broilers_marsh = dup_broilers_marsh , chick_marsh = dup_chick_marsh , 
                                    old_pig = dup_old_pig , growers_marsh = dup_growers_marsh,layers_marsh = dup_layers_marsh , young_pig = dup_young_pig)
    else:
        print("Why can't just be free , from the ways of this world")

    last_rm_quantity = RawMaterialPrices.objects.last()
    #check if it has any instances , if not then just skip to the end
    count_rm = RawMaterialPrices.objects.count()
    if(count_rm != 0):
        #change dates into some specific dates (%x-Local version of date-12/31/18)
        last_date = last_rm_quantity.date
        rear_date = last_date.strftime("%x")
        current_date = datetime.datetime.now()
        earlist_date = current_date.strftime("%x")
        if rear_date == earlist_date:
            print("Dates are equal")
        else:
            #duplicate the last instance
            dup_maize_bran = last_raw_material_qty_occurance.maize_bran 
            dup_cotton = last_raw_material_qty_occurance.cotton
            dup_sun_flower = last_raw_material_qty_occurance.sun_flower
            dup_fish = last_raw_material_qty_occurance.fish
            
            dup_general_purpose_premix = last_raw_material_qty_occurance.general_purpose_premix
            dup_layers_premix = last_raw_material_qty_occurance.layers_premix
            dup_shells = last_raw_material_qty_occurance.shells
            dup_meat_boaster = last_raw_material_qty_occurance.meat_boaster
            dup_egg_boaster=last_raw_material_qty_occurance.egg_boaster
            duplicate_quantiites = RawMaterialPrices.objects.create(date = datetime.datetime.now(),maize_bran = dup_maize_bran ,cotton = dup_cotton,
                                                                   sun_flower = dup_sun_flower, fish = dup_fish,
                                                                   general_purpose_premix = dup_general_purpose_premix,layers_premix = dup_layers_premix,
                                                                   shells = dup_shells, meat_boaster = dup_meat_boaster,egg_boaster=dup_egg_boaster)
    else:
        print("Just continue with life")
    # Viewing the product quantities
    # last item represents the raw material quantities
    # last product represent the product quantities

    # now we are going to get the income statement
    # Net income/loss = product_sales + raw_material_sales - expenses
    # revenue = product_sales + raw_material_sales 
    # profit / loss = sales  - expenses

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    #Products
    # p_sales = ProductSales.objects.values_list('total', 'date =[start_date, end_date]')
    p_sales = ProductSales.objects.filter(date__range=[start_date, end_date])
    # last_sale = last_product_sale.total
    #Have a list containing all the product sales 
    p_sale_list = []
    #get each sale
    for p_sale in p_sales:
        p_sale_list.append(p_sale.total)
    #then sum up the list 
    product_sales = sum(p_sale_list)
    #Raw materials
    rm_sales = RawMaterialSales.objects.filter(date__range=[start_date, end_date])
    # last_r_m_sale = last_raw_material_sale.total
    #a list containing all raw material sales
    rm_sale_list = []
    #get each sale
    for rm_sale in rm_sales:
        rm_sale_list.append(rm_sale.total)
    #then sum up the list
    raw_material_sales = sum(rm_sale_list)

    #expenses
    expenses = Expenses.objects.filter(date__range=[start_date, end_date])
    # last_expense = last_expenses.total
    #list of expenses
    expenses_list = []
    #use a loop to get total of every expense
    for expense in expenses:
        #add that expense total into the 'expenses_list'
        expenses_list.append(expense.amount)
    #sum up all the 'expense total' in that 'expenses_list'
    sum_of_expenses = sum(expenses_list)
    
    #net income 

    net_income = (product_sales + raw_material_sales) - sum_of_expenses

    selected_date = request.GET.get('selected_date')

    raw_material_inventory = RawMaterialQuantities.objects.filter(date=selected_date)

    return render(request, "index.html",{'last_raw_material_qty_occurance':last_raw_material_qty_occurance,'lastproduct':lastproduct,'product_sales':product_sales,
    'raw_material_sales':raw_material_sales,'sum_of_expenses':sum_of_expenses,'net_income':net_income } )

def creating_net_income(request):
    #now we are going to get the income statement # Net income/loss = product_sales + raw_material_sales - expenses # revenue = product_sales + raw_material_sales 
    # profit / loss = sales  - expenses
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    #Products
    # p_sales = ProductSales.objects.values_list('total', 'date =[start_date, end_date]')
    p_sales = ProductSales.objects.filter(date__range=[start_date, end_date])
    # last_sale = last_product_sale.total
    #Have a list containing all the product sales 
    p_sale_list = []
    #get each sale
    for p_sale in p_sales:
        p_sale_list.append(p_sale.total)
    #then sum up the list 
    product_sales = sum(p_sale_list)
    #Raw materials
    rm_sales = RawMaterialSales.objects.filter(date__range=[start_date, end_date])
    # last_r_m_sale = last_raw_material_sale.total
    #a list containing all raw material sales
    rm_sale_list = []
    #get each sale
    for rm_sale in rm_sales:
        rm_sale_list.append(rm_sale.total)
    #then sum up the list
    raw_material_sales = sum(rm_sale_list)
    #expenses
    expenses = Expenses.objects.filter(date__range=[start_date, end_date])
    # last_expense = last_expenses.total
    #list of expenses
    expenses_list = []
    #use a loop to get total of every expense
    for expense in expenses:
        #add that expense total into the 'expenses_list'
        expenses_list.append(expense.total)
    #sum up all the 'expense total' in that 'expenses_list'
    sum_of_expenses = sum(expenses_list)
    
    #net income 

    net_income = (product_sales + raw_material_sales) - sum_of_expenses

    return render(request,'index.html',{'products_sales':product_sales,
    'raw_material_sales':raw_material_sales,'sum_of_expenses':sum_of_expenses,'net_income':net_income})

def creating_supplies(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    supply_form = RawMaterialForm(request.POST or None)
    # expense_form = ExpenseForm(request.POST or None)
    if request.method == 'POST':
        # add the dictionary during initialization
        if supply_form.is_valid():

            supply_form.save()
            # expense_form.save()
            #Its here that after the supply is made then we shall start populating the RawMaterialQuantities
            #table
            # we shall check if the "RawMaterialQuantities" table has atleast one row
            compute_quantities()       
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        context['supply_form'] = supply_form
        # context['expense_form'] = expense_form
    return render(request, "supply.html",{'supply_form':supply_form})

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
                # update_quantites(increase_quantity_value,reduce_quantity_value , form)
                increment_quantities(increase_quantity_value,form)
                decrement_quantities(reduce_quantity_value,form)
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

def create_product(request):
    context = {}
    form = ProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            product = form.cleaned_data['product']  
            maize_bran = form.cleaned_data['maize_bran']
            cotton = form.cleaned_data['cotton']
            sun_flower = form.cleaned_data['sun_flower']
            fish = form.cleaned_data['fish']
            general_purpose_premix = form.cleaned_data['general_purpose_premix']
            layers_premix = form.cleaned_data['layers_premix']
            shells = form.cleaned_data['shells']
            meat_boaster = form.cleaned_data['meat_boaster']
            egg_boaster = form.cleaned_data['egg_boaster']
            
            calcium = form.cleaned_data['calcium'] 
            soya_bean = form.cleaned_data['soya_bean']
            animal_salt = form.cleaned_data['animal_salt']
            common_salt = form.cleaned_data['common_salt']
            brown_salt = form.cleaned_data['brown_salt']
            coconut = form.cleaned_data['coconut']
            pig_concentrate = form.cleaned_data['pig_concentrate']
            wonder_pig = form.cleaned_data['wonder_pig']
            big_pig = form.cleaned_data['big_pig']

            # maize_bran,cotton,sun_flower,fish,salt,general_purpose_premix,layers_premix ,shells 
            # ,meat_boaster ,egg_boaster

            check_if_product_quantities_are_empty()
             
            subtracting(maize_bran,cotton,sun_flower,fish,general_purpose_premix,layers_premix,shells,meat_boaster,egg_boaster,calcium,soya_bean,animal_salt,common_salt,brown_salt,coconut,pig_concentrate,wonder_pig,big_pig)

            #populate the product quantities model

            adding(
                 product
                ,maize_bran
                ,cotton
                ,sun_flower
                ,fish
                ,general_purpose_premix
                ,layers_premix
                ,shells,meat_boaster
                ,egg_boaster
                ,calcium
                ,soya_bean
                ,animal_salt
                ,common_salt
                ,brown_salt
                ,coconut
                ,pig_concentrate
                ,wonder_pig
                ,big_pig
                )

            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:        
        context['form'] = form
    

    return render(request,"product.html",context)

def viewing_product(request):
    #get the date from the user 
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    # six_months.strftime('%Y%m%d')
    # run a query to get all the supplies on that date
    products = Product.objects.filter(date__range=[start_date, end_date])
    print(type(products))   
    return render(request, "view_products.html", {'products':products}) 

def updating_product(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        product_record = Product.objects.get(id=clean_pk)
        form = ProductForm(request.POST or None, instance=product_record)
        if request.method == 'POST':
            if form.is_valid():
            
                form.save()

                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 
            
    return render(request,"update_products.html",context=context_dict)

def deleting_product(request):
    # book= get_object_or_404(Book, pk=pk)  
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        product_record_to_delete = Product.objects.get(id=cleaned_pk)  
        if request.method=='POST':
            product_record_to_delete.delete()
            return HttpResponseRedirect('http://127.0.0.1:8000/')   

    return render(request, "delete_products.html",context=context_dict)

def create_raw_material_prices(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = RawMaterialPricesForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            #Its here that after the supply is made then we shall start populating the RawMaterialQuantities
            #table
            # we shall check if the "RawMaterialQuantities" table has atleast one row
            # compute_quantities()  
            return HttpResponseRedirect('http://127.0.0.1:8000/')       
    else:
        context['form'] = form

    return render(request, "create_raw_material_prices.html",context)

def viewing_raw_material_prices(request):
    #get the date from the user 
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

    # run a query to get all the supplies on that date
    p_prices = RawMaterialPrices.objects.filter(date__range=[start_date, end_date])

    # print(type(supplies))
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_raw_material_prices.html", {'p_prices':p_prices})

def updating_raw_material_prices(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        product_prices = RawMaterialPrices.objects.get(id=clean_pk)
        form = RawMaterialPricesForm(request.POST or None, instance=product_prices)
        
        if request == 'POST':
            if form.is_valid():         
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
                
        else:
            context_dict["form"] = form

    return render(request,"update_raw_material_prices.html",context=context_dict)

def deleting_raw_material_prices(request):
     # book= get_object_or_404(Book, pk=pk)  
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        product_price_to_delete = RawMaterialPrices.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        product_price_to_delete.delete()

        # return HttpResponseRedirect('http://127.0.0.1:8000/')
        # redirect('view_product_prices.html')
        # if request.method =='POST':
        #   #we get to know the item 

        #     supply_record_to_delete.delete()
        #     return redirect('view_supply.html')

        # context_dict["object"] = supply_record_to_delete
    return render(request, "delete_raw_material_prices.html",context=context_dict)

def creating_product_prices(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = ProductPriceForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            #Its here that after the supply is made then we shall start populating the RawMaterialQuantities
            #table
            # we shall check if the "RawMaterialQuantities" table has atleast one row
            # compute_quantities()  
            return HttpResponseRedirect('http://127.0.0.1:8000/')       
    else:
        context['form'] = form
    return render(request, "create_product_price.html",context)

def viewing_product_prices(request):
    #get the date from the user 
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

    # run a query to get all the supplies on that date
    p_prices = ProductPrices.objects.filter(date__range=[start_date, end_date])

    # print(type(supplies))
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_product_prices.html", {'p_prices':p_prices})

def updating_product_prices(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        product_prices = ProductPrices.objects.get(id=clean_pk)
        form = ProductPriceForm(request.POST or None, instance=product_prices)
    
        # if request == 'POST':
        #     if form.is_valid():                
        #         form.save()
        #         return HttpResponseRedirect('http://127.0.0.1:8000/')       
        # else:
        #     context_dict["form"] = form
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                #Its here that after the supply is made then we shall start populating the RawMaterialQuantities
                #table
                # we shall check if the "RawMaterialQuantities" table has atleast one row
                # compute_quantities()  
                return HttpResponseRedirect('http://127.0.0.1:8000/')       
        else:
            context['form'] = form
    return render(request,"update_product_prices.html",context=context_dict)

def deleting_product_prices(request):
    # book= get_object_or_404(Book, pk=pk)  
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        product_price_to_delete = ProductPrices.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        product_price_to_delete.delete()
        
        # if request.method =='POST':
        #   #we get to know the item 

        #     supply_record_to_delete.delete()
        #     return redirect('view_supply.html')

        # context_dict["object"] = supply_record_to_delete
    return render(request, "delete_product_prices.html",context=context_dict)

def doing_product_sales(request):
    #get the date from the user 
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

    # run a query to get all the supplies on that date
    p_q = ProductQuantities.objects.filter(date__range=[start_date, end_date])

    l_p_q = ProductQuantities.objects.last()

    l_p_p = ProductPrices.objects.last()

    context = {}
    # add the dictionary during initialization
    form = ProductSalesForm(request.POST or None)

    # if request.method == 'POST':
    if form.is_valid():
        #So here it means that if am deduct the quantity that has been bought,
        #i must do it for every raw material , that's what it means 
        # Get to know the particular product from the form
        product = form.cleaned_data['product']
        quantity = form.cleaned_data['quantity']    
        print("Hello we are now here")
        product_sales_quantity_deduction(product,quantity)        
        form.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/')       

    #Adding items to the dictionary
    context['form'] = form
    context['p_q'] = p_q
    context['l_p_q'] = l_p_q
    context['l_p_p'] = l_p_p

    return render(request, "do_product_sales.html", context)

def viewing_product_sales(request):
    #get the date from the user 
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

    # run a query to get all the supplies on that date
    p_sales = ProductSales.objects.filter(date__range=[start_date, end_date])
    
    broilers_marsh_list = []
    chick_marsh_list = []
    growers_marsh_list = []
    old_pig_list = []
    layers_marsh_list = []
    young_pig_list = []

    for sale in p_sales:
        if sale.product == "broilers_marsh":
            broilers_marsh_list.append(sale.quantity)

        elif sale.product == "chick_marsh":
            chick_marsh_list.append(sale.quantity)

        elif sale.product == "growers_marsh": 
            growers_marsh_list.append(sale.quantity)

        elif sale.product == "old_pig":
            old_pig_list.append(sale.quantity)

        elif sale.product == "layers_marsh":
            layers_marsh_list.append(sale.quantity)

        elif sale.product == "young_pig":
            young_pig_list.append(sale.quantity)

    #summation of product sales into a dictionary
    product_sales_dictionary = {}

    product_sales_dictionary["broilers_marsh"] = sum(broilers_marsh_list)
    product_sales_dictionary["chick_marsh"] = sum(chick_marsh_list)
    product_sales_dictionary["growers_marsh"] = sum(growers_marsh_list)
    product_sales_dictionary["old_pig"] = sum(old_pig_list)
    product_sales_dictionary["layers_marsh"] = sum(layers_marsh_list)
    product_sales_dictionary["young_pig"] = sum(young_pig_list)
    return render(request, "view_product_sales.html", {'p_sales':p_sales,'product_sales_dictionary':product_sales_dictionary})

def updating_product_sales(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        product_record = ProductSales.objects.get(id=clean_pk)
        form = ProductSalesForm(request.POST or None, instance=product_record)
        if request.method == 'POST':
            if form.is_valid():
            
                form.save()

                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 
    return render(request,"update_product_sales.html",context=context_dict)

def deleting_product_sales(request):
    # book= get_object_or_404(Book, pk=pk)  
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        product_sale_to_delete = ProductSales.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        product_sale_to_delete.delete()
        
        # if request.method =='POST':
        #   #we get to know the item 

        #     supply_record_to_delete.delete()
        #     return redirect('view_supply.html')

        # context_dict["object"] = supply_record_to_delete
    return render(request, "delete_product_sales.html",context=context_dict)

def doing_raw_material_sales(request):
    #get the date from the user 
    # broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

    # run a query to get all the supplies on that date

    last_raw_material_quantity = RawMaterialQuantities.objects.last()

    last_raw_material_prices = RawMaterialPrices.objects.last()

    context = {}
    # add the dictionary during initialization
    form = RawMaterialSalesForm(request.POST or None)
    if request.method == 'POST':


        if form.is_valid():
            # So here it means that if am deduct the quantity that has been bought,
            # i must do it for every raw material , that's what it means 
            # raw_material = form.cleaned_data['raw_material']
            # quantity = form.cleaned_data['quantity']
            # raw_material_sales_quantity_deduction(raw_material,quantity)
            raw_material = form.cleaned_data['raw_material']
            quantity = form.cleaned_data['quantity']  
            raw_material_sales_quantity_deduction(raw_material,quantity)
            form.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form
    # So am suggesting that after the sale has been saved , then we deduct the quantities 
    # last_sale = RawMaterialSales.objects.last()
    #then throw the variables to the deduction function
    # raw_material_sales_quantity_deduction(last_sale.raw_material,last_sale.quantity)


    return render(request, "do_raw_material_sales.html", {'last_raw_material_quantity':last_raw_material_quantity,'last_raw_material_prices':last_raw_material_prices ,'form':form ,})

def viewing_raw_material_sales(request):
    #get the date from the user 
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    raw_material_sales_dictionary = {}

    # broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 
    # run a query to get all the supplies on that date
    rm_sales = RawMaterialSales.objects.filter(date__range=[start_date, end_date])

    maize_bran_list = []
    cotton_list = []
    sun_flower_list = []
    fish_list = []
    general_purpose_premix_list = []
    layers_premix_list = []
    shells_list = []
    meat_boaster_list = []
    egg_boaster_list =[]
    calcium_list = []
    soya_bean_list = []
    brown_salt_list = []
    animal_salt_list = []
    common_salt_list = []
    pig_concentrate_list = []
    coconut_list = []
    wonder_pig_list = []
    big_pig_list= []

    for sale in rm_sales:
        if sale.raw_material == "maize_bran":
            maize_bran_list.append(sale.quantity)
    
        elif sale.raw_material == "cotton":
            cotton_list.append(sale.quantity)
            
        elif sale.raw_material == "sun_flower":
            sun_flower_list.append(sale.quantity)

        elif sale.raw_material == "fish":
            fish_list.append(sale.quantity)

        elif sale.raw_material == "general_purpose_premix":
            general_purpose_premix_list.append(sale.quantity)

        elif sale.raw_material == "shells":
            shells_list.append(sale.quantity)

        elif sale.raw_material == "meat_boaster":
            meat_boaster_list.append(sale.quantity)

        elif sale.raw_material == "egg_boaster":
            egg_boaster_list.append(sale.quantity)

        elif sale.raw_material == "calcium":
            calcium_list.append(sale.quantity)

        elif sale.raw_material == "soya_bean":
            soya_bean_list.append(sale.quantity)

        elif sale.raw_material == "brown_salt":
            brown_salt_list.append(sale.quantity)

        elif sale.raw_material == "animal_salt":
            animal_salt_list.append(sale.quantity)

        elif sale.raw_material == "common_salt":
            common_salt_list.append(sale.quantity)

        elif sale.raw_material == "cotton":
            cotton_list.append(sale.quantity)

        elif sale.raw_material == "pig_concentrate":
            pig_concentrate_list.append(sale.quantity)

        elif sale.raw_material == "coconut":
            coconut.append(sale.quantity)

        elif sale.raw_material == "wonder_pig":
            wonder_pig_list.append(sale.quantity)

        elif sale.raw_material == "big_pig":
            big_pig_list.append(sale.quantity)
    # print(type(supplies))     
    # return render(request, "view_supply.html", context)

    #Now we are going to find the summation of all the lists and then put them in a list too

    raw_material_sales_dictionary = {} 

    #Add the different summations to the dictionary
    raw_material_sales_dictionary["maize_bran"] = sum(maize_bran_list)
    raw_material_sales_dictionary["cotton"] = sum(cotton_list)
    raw_material_sales_dictionary["sun_flower"] = sum(sun_flower_list)
    raw_material_sales_dictionary["fish"] = sum(fish_list)
    raw_material_sales_dictionary["general_purpose_premix"] = sum(general_purpose_premix_list)
    raw_material_sales_dictionary["layers_premix"] = sum(layers_premix_list)
    raw_material_sales_dictionary["shells"] = sum(shells_list)
    raw_material_sales_dictionary["meat_boaster"] = sum(meat_boaster_list)
    raw_material_sales_dictionary["egg_boaster"] = sum(egg_boaster_list)
    raw_material_sales_dictionary["calcium"] = sum(calcium_list)
    raw_material_sales_dictionary["soya_bean"] = sum(soya_bean_list)
    raw_material_sales_dictionary["brown_salt"] = sum(brown_salt_list)
    raw_material_sales_dictionary["common_salt"] = sum(common_salt_list)
    raw_material_sales_dictionary["pig_concentrate"] = sum(pig_concentrate_list)
    raw_material_sales_dictionary["coconut"] = sum(coconut_list)
    raw_material_sales_dictionary["wonder_pig"] = sum(wonder_pig_list)
    raw_material_sales_dictionary["big_pig"] = sum(big_pig_list)

    print (raw_material_sales_dictionary)
    return render(request, "view_raw_material_sales.html", {'rm_sales':rm_sales , 'raw_material_sales_dictionary':raw_material_sales_dictionary})

def updating_raw_material_sales(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        raw_material_record = RawMaterialSales.objects.get(id=clean_pk)
        form = RawMaterialSalesForm(request.POST or None, instance=raw_material_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 
    return render(request,"update_raw_material_sales.html",context=context_dict)

def deleting_raw_material_sales(request):
    # book= get_object_or_404(Book, pk=pk)  
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        raw_material_sale_to_delete = RawMaterialSales.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
        raw_material_sale_to_delete.delete()
        
        # if request.method =='POST':
        #   #we get to know the item 

        #     supply_record_to_delete.delete()
        #     return redirect('view_supply.html')

        # context_dict["object"] = supply_record_to_delete
    return render(request, "delete_raw_material_sales.html",context=context_dict)

def getting_expenses(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # supply_form = SupplyForm(request.POST or None)
    expense_form = ExpenseForm(request.POST or None)
    if request.method == 'POST':
        # add the dictionary during initialization
        if expense_form.is_valid():
            # supply_form.save()
            expense_form.save()
            #Its here that after the supply is made then we shall start populating the RawMaterialQuantities
            #table
            # we shall check if the "RawMaterialQuantities" table has atleast one row
            # compute_quantities()
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        # context['supply_form'] = supply_form
        context['expense_form'] = expense_form
    return render(request, "expense.html",{'expense_form':expense_form})

def viewing_expenses(request):
    #get the date from the user 
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

    # run a query to get all the supplies on that date
    daily_expenses = Expenses.objects.filter(date__range=[start_date, end_date])
    # print(type(supplies))     
    # return render(request, "view_supply.html", context)
    return render(request, "view_expenses.html", {'daily_expenses':daily_expenses})

def updating_expenses(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        expenses_record = Expenses.objects.get(id=clean_pk)
        form = ExpenseForm(request.POST or None, instance=expenses_record)
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return HttpResponseRedirect('http://127.0.0.1:8000/')   
        else:
            context_dict["form"] = form 
    return render(request,"update_expenses.html",context=context_dict)

def deleting_expenses(request):
    # book= get_object_or_404(Book, pk=pk)  
    context_dict = {}
    if 'id' in request.GET:
        pk = request.GET['id']
        clean_pk = pk.strip("/")
        cleaned_pk = int(clean_pk)
        expense_to_delete = Expenses.objects.get(id=cleaned_pk) 
        #But before we delete , we must reduce on the amount in the RMQ model
        #since this is an object , i will create a function right away
        
    expense_to_delete.delete()
        
    return render(request, "delete_expenses.html",context=context_dict)