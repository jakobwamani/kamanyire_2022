from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from feedwork.models import *
from feedwork.forms import *
from feedwork.helper_functions import * 
from django.http import HttpResponseRedirect


def index(request):
    # return HttpResponse("Hello, world. You're at the STS Poultry Business ")
    #To create a new instance of the RMQ model 
    #grab the lastest instance inside the RMQ model
    lastitem = RawMaterialQuantities.objects.last()
    #check if it has any instances , if not then just skip to the end
    count_quantities = RawMaterialQuantities.objects.count()
    if(count_quantities != 0):
        #change dates into some specific dates (%x-Local version of date-12/31/18)
        last_date = lastitem.date
        rear_date = last_date.strftime("%x")
        current_date = datetime.datetime.now()
        earlist_date = current_date.strftime("%x")
        if rear_date == earlist_date:
            print("Dates are equal")
        else:
            #duplicate the last instance
            dup_maize_bran = lastitem.maize_bran 
            dup_cotton = lastitem.cotton
            dup_sun_flower = lastitem.sun_flower
            dup_fish = lastitem.fish
            dup_salt = lastitem.salt
            dup_general_purpose_premix = lastitem.general_purpose_premix
            dup_layers_premix = lastitem.layers_premix
            dup_shells = lastitem.shells
            dup_meat_boaster = lastitem.meat_boaster
            dup_egg_boaster=lastitem.egg_boaster
            dup_calcium = lastitem.calcium
            dup_soya_bean = lastitem.soya_bean
            dup_brown_salt = lastitem.brown_salt
            dup_animal_salt = lastitem.animal_salt
            dup_common_salt = lastitem.common_salt 
            dup_coconut = lastitem.coconut 
            dup_pig_concentrate = lastitem.pig_concentrate
            dup_wonder_pig = lastitem.wonder_pig 
            dup_big_pig = lastitem.big_pig 


            duplicate_quantiites = RawMaterialQuantities.objects.create(date = datetime.datetime.now(),maize_bran = dup_maize_bran ,cotton = dup_cotton,
                                                                   sun_flower = dup_sun_flower, fish = dup_fish,salt = dup_salt ,
                                                                   general_purpose_premix = dup_general_purpose_premix,layers_premix = dup_layers_premix,
                                                                   shells = dup_shells, meat_boaster = dup_meat_boaster,egg_boaster=dup_egg_boaster
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
            dup_maize_bran = lastitem.maize_bran 
            dup_cotton = lastitem.cotton
            dup_sun_flower = lastitem.sun_flower
            dup_fish = lastitem.fish
            dup_salt = lastitem.salt
            dup_general_purpose_premix = lastitem.general_purpose_premix
            dup_layers_premix = lastitem.layers_premix
            dup_shells = lastitem.shells
            dup_meat_boaster = lastitem.meat_boaster
            dup_egg_boaster=lastitem.egg_boaster
            duplicate_quantiites = RawMaterialPrices.objects.create(date = datetime.datetime.now(),maize_bran = dup_maize_bran ,cotton = dup_cotton,
                                                                   sun_flower = dup_sun_flower, fish = dup_fish,salt = dup_salt ,
                                                                   general_purpose_premix = dup_general_purpose_premix,layers_premix = dup_layers_premix,
                                                                   shells = dup_shells, meat_boaster = dup_meat_boaster,egg_boaster=dup_egg_boaster)
    else:
        print("Just continue with life")
    


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
            salt = form.cleaned_data['salt']
            general_purpose_premix = form.cleaned_data['general_purpose_premix']
            layers_premix = form.cleaned_data['layers_premix']
            shells = form.cleaned_data['shells']
            meat_boaster = form.cleaned_data['meat_boaster']
            egg_boaster = form.cleaned_data['egg_boaster']
            # Raw Materials to be added
            calcium = form.cleaned_data['calcium'] 
            soya_bean = form.cleaned_data['soya_bean']
            animal_salt = form.cleaned_data['animal_salt']
            common_salt = form.cleaned_data['common_salt']
            coconut = form.cleaned_data['coconut']
            pig_concentrate = form.cleaned_data['pig_concentrate']
            wonder_pig = form.cleaned_data['wonder_pig']
            big_pig = form.cleaned_data['big_pig']

            # maize_bran,cotton,sun_flower,fish,salt,general_purpose_premix,layers_premix ,shells 
            # ,meat_boaster ,egg_boaster
             
            subtracting(product,maize_bran,cotton,sun_flower,fish,salt,general_purpose_premix,layers_premix,shells,meat_boaster,egg_boaster,calcium,soya_bean,animal_salt,common_salt,coconut,pig_concentrate,wonder_pig,big_pig)

            #populate the product quantities model

            adding(product,maize_bran,cotton,sun_flower,fish,salt,general_purpose_premix,layers_premix,shells,meat_boaster,egg_boaster,calcium,soya_bean,animal_salt,common_salt,coconut,pig_concentrate,wonder_pig,big_pig)

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