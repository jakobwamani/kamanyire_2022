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
    check_if_raw_material_quantities_are_empty()
    if_its_a_newday()
    
    #Now we are going to view the raw material quantites by date
  
    if request.method == 'POST':
        raw_material_stock = {}
        selected_date = request.POST.get('start_date')
        
        raw_material_stock = RawMaterialQuantities.objects.filter(date=selected_date).last()
        

        #display the product quantities
        choosen_date = request.POST.get('choosen_date')
        product_stock = ProductQuantities.objects.filter(date=choosen_date).last()
        print(product_stock)

        print(raw_material_stock)

       
        # select profits of raw materials

        selected_date = request.POST.get('select_date')
        raw_material_profits = RawMaterialProfits.objects.filter(date=selected_date).last()

        
        # print("Working on product profits now")
        picked_date = request.POST.get('pick_date')
        product_profits = ProductProfits.objects.filter(date=picked_date).last()

    

        return render(request, "index.html",{'raw_material_stock':raw_material_stock,'raw_material_profits':raw_material_profits,'product_stock':product_stock , 'product_profits':product_profits} )
    else:
        return render(request,"index.html",{})
def creating_net_income(request):
    #now we are going to get the income statement # Net income/loss = product_sales + raw_material_sales - expenses # revenue = product_sales + raw_material_sales 
    # profit / loss = sales  - expenses
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
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
            #Accessing the date field 
            # product = supply_form.cleaned_data['date']
            print(supply_form)
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
@snoop
def viewing_supplies(request):
    #get the date from the user 
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    raw_material = request.POST.get('raw_material_option')

    # run a query to get all the supplies on that date
    supplies = RawMaterial.objects.filter(date__range=[start_date, end_date]).filter(item=raw_material)

    print(supplies)
    #To get the total we have to get a sum of totals from a specific queryset
    total_sales = []
    for supply in supplies:
        # summation = (supply.quantity * supply.unit_price) + supply.transport + supply.off_loading + supply.loading
        total_sales.append(supply.total)

    sales_money = sum(total_sales)
     
    print(sales_money)
    # return render(request, "view_supply.html", context)
    return render(request, "view_supplies.html", {'supplies':supplies ,'sales_money':sales_money})

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
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    # six_months.strftime('%Y%m%d')
    # run a query to get all the supplies on that date
    products = Product.objects.filter(date__range=[start_date, end_date]).filter()
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

@snoop
def doing_product_sales(request):
    #get the date from the user 
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

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
        picked_date = form.cleaned_data['date']
        product = form.cleaned_data['product']
        quantity = form.cleaned_data['quantity']    
        print("Hello we are now here")
        product_sales_quantity_deduction(product,quantity)        
        form.save()

        #calculating profit
        processed_profit = process_product_profits(picked_date,product)
        print(processed_profit)

        last_profit = ProductProfits.objects.last()

        last_profit.pk = None
        last_profit.save()
        #then again create the latest profit 
        lastest_profit = ProductProfits.objects.last()

        lastest_profit = ProductProfits.objects.last()
        #loop through it to get the current profit of a specific raw_material
        for attr , value in vars(lastest_profit).items():
            if attr == product:
                #then we change the value
                # value = profit 
                # thisdict["year"] = 2018
                vars(lastest_profit)[attr] = processed_profit 
                lastest_profit.date = datetime.date.today() 
                lastest_profit.time = timezone.now()
                lastest_profit.save()
        
        return HttpResponseRedirect('http://127.0.0.1:8000/')       

    #Adding items to the dictionary
    context['form'] = form
    context['p_q'] = p_q
    context['l_p_q'] = l_p_q
    context['l_p_p'] = l_p_p

    return render(request, "do_product_sales.html", context)

def viewing_product_sales(request):
    #get the date from the user 
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    picked_product = request.POST.get('product_option')
    # broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

    # run a query to get all the supplies on that date
    p_sales = ProductSales.objects.filter(date__range=[start_date, end_date]).filter(product=picked_product)
    print(p_sales)
    broilers_marsh_list = []
    chick_marsh_list = []
    growers_marsh_list = []
    
    layers_marsh_list = []
    pig_marsh_list = []

    for sale in p_sales:
        if sale.product == "broilers_marsh":
            broilers_marsh_list.append(sale.quantity)

        elif sale.product == "chick_marsh":
            chick_marsh_list.append(sale.quantity)

        elif sale.product == "growers_marsh": 
            growers_marsh_list.append(sale.quantity)

        elif sale.product == "layers_marsh":
            layers_marsh_list.append(sale.quantity)

        elif sale.product == "pig_marsh":
            pig_marsh_list.append(sale.quantity)

    #summation of product sales into a dictionary
    product_sales_dictionary = {}

    product_sales_dictionary["broilers_marsh"] = sum(broilers_marsh_list)
    product_sales_dictionary["chick_marsh"] = sum(chick_marsh_list)
    product_sales_dictionary["growers_marsh"] = sum(growers_marsh_list)
    # product_sales_dictionary["old_pig"] = sum(old_pig_list)
    product_sales_dictionary["layers_marsh"] = sum(layers_marsh_list)
    product_sales_dictionary["pig_marsh"] = sum(pig_marsh_list)

    #Discover the total sales per product 
    #Create a list
    sales_summation = []
    for sale in p_sales:
        sales_summation.append(sale.total)

    total_sales = sum(sales_summation)
    return render(request, "view_product_sales.html", {'p_sales':p_sales,'product_sales_dictionary':product_sales_dictionary,'total_sales':total_sales})

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

@snoop
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
            date = form.cleaned_data['date']
            raw_material = form.cleaned_data['raw_material']
            quantity = form.cleaned_data['quantity']  
            raw_material_sales_quantity_deduction(raw_material,quantity)
            form.save()
            #calculate the profit this function returns a profit
            profit = profits_for_raw_materials(date,raw_material)
            print(profit)
            #then save to the raw_material profits table

            #create an occurance into the profits table
            #get the last occurance 
            last_profit = RawMaterialProfits.objects.last()
            #create a duplicate
            last_profit.pk = None
            last_profit.save()
            #then again create the latest profit 
            lastest_profit = RawMaterialProfits.objects.last()
            #loop through it to get the current profit of a specific raw_material
            for attr , value in vars(lastest_profit).items():
                if attr == raw_material:
                    #then we change the value
                    # value = profit 
                    # thisdict["year"] = 2018
                    vars(lastest_profit)[attr] = profit 
                    lastest_profit.date = datetime.date.today() 
                    lastest_profit.time = timezone.now()
                    lastest_profit.save()


            

            return HttpResponseRedirect('http://127.0.0.1:8000/') 
    else:
        context['form'] = form
    # So am suggesting that after the sale has been saved , then we deduct the quantities 
    # last_sale = RawMaterialSales.objects.last()
    #then throw the variables to the deduction function
    # raw_material_sales_quantity_deduction(last_sale.raw_material,last_sale.quantity)

    #if when the raw material sale is made , then we calculate the profit there and then

    return render(request, "do_raw_material_sales.html", {'last_raw_material_quantity':last_raw_material_quantity,'last_raw_material_prices':last_raw_material_prices ,'form':form ,})

@snoop
def viewing_raw_material_sales(request):
    #get the date from the user 
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    selected_raw_material = request.POST.get('pick_raw_material')
    raw_material_sales_dictionary = {}

    # broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 
    # run a query to get all the supplies on that date
    rm_sales = RawMaterialSales.objects.filter(date__range=[start_date, end_date]).filter(raw_material=selected_raw_material)

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
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    # broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh ,young_pig 

    # run a query to get all the supplies on that date
    daily_expenses = Expenses.objects.filter(date__range=[start_date, end_date])
    
    #showing Total of expenses
    expense_list = []
    for expense in daily_expenses:
        expense_list.append(expense.amount)

    sum_of_expenses = sum(expense_list)

    return render(request, "view_expenses.html", {'daily_expenses':daily_expenses,'sum_of_expenses':sum_of_expenses})

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
    employees = employee_enrollment.objects.filter(date__range=[start_date, end_date])
     
    # return render(request, "view_supply.html", context)
    return render(request, "view_employees.html", {'employees':employees})

def update_employees(request):
    context_dict = {}

    if 'id' in request.GET:
        pk = request.GET['id']

        print (pk)
        clean_pk = pk.strip("/")
        print (clean_pk)
        employee_record = employee_enrollment.objects.get(id=clean_pk)
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
