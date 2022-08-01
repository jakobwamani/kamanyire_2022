from requests import request
from feedwork.models import *
import datetime
from django.db.models import Q
# Import statistics Library
import statistics
import snoop
from django.utils import timezone

def compute_quantities():
   check_row = RawMaterialQuantities.objects.count()

   if check_row >= 1:
      #here am going to introduct a function because item get the item that has been supplied
      #but first , i need to get it from the form
      #so here due the technical difficulty we shall not care to find out which specific item
      #at first was supplied   
      # we also have to check if the Raw material model is populated or not
      check_supplies = RawMaterial.objects.count()

      if check_supplies >= 1: 
         #we get a list of all the raw materials
         raw_material_list = ['maize_bran','cotton','sun_flower','fish','layers_premix','general_purpose_premix','shells','meat_boaster','egg_boaster','pig_concentrate','soya_bean','calcium','brown_salt','brown_salt','animal_salt','common_salt','coconut','pig_concentrate','wonder_pig','big_pig']
         #we get the last entry 
         get_lastest_item_supplied = RawMaterial.objects.last()
         quantity_of_lastest_item  = get_lastest_item_supplied.quantity
         lastest_item_supplied     = get_lastest_item_supplied.item
         for element in raw_material_list:
            if lastest_item_supplied == element:
               quantity = RawMaterialQuantities.objects.last()
               for attr, value in vars(quantity).items():
                  print(attr, '=', value)
               
                  if attr == element:
                     print("Its a match")
                     print(value)
                     current_quantity = value

                     total_quantity = current_quantity + quantity_of_lastest_item

                     #create a duplicate copy of the last instance
                     quantity.pk = None
                     quantity.save()
                     #but then update the quantity that has been provided
                     duplicate_quantity = RawMaterialQuantities.objects.last()
                     print(duplicate_quantity)
                     #that's when i will update it the specified quantity
                     for attr , value in vars(duplicate_quantity).items():
                        print(attr, '=', value)
                        if attr == element:
                           vars(duplicate_quantity)[attr] = total_quantity 
                           print(vars(duplicate_quantity)[attr])
                           #then save
                           duplicate_quantity.save()
         #we want to get the lastest value of a specific item
         #We just look through the RawMaterial model and look for last input of a specific item
         # get_lastest_item_supplied = RawMaterial.objects.latest('-item')
         # get_lastest_item_supplied = RawMaterial.objects.last()
         # quantity_of_lastest_item  = get_lastest_item_supplied.quantity
         # lastest_item_supplied     = get_lastest_item_supplied.item
         # #use these two variables quantity_of_lastest_item and lastest_item_supplied to update the row
         # # the RawMaterialQuantities model
         # if lastest_item_supplied == 'maize_bran':
         #    #get the current values inside the RawMaterialQuantities
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.maize_bran
         #    #now add both quantities from the Raw material table and RawMaterialQuantities table
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    #then now i can update the value inside the RawMaterialQuantites model       
         #    # #i proceed to update the RMQ table
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.maize_bran = total_quantity
         #    quantity_addition.save() 

         # elif lastest_item_supplied == 'cotton':
         #    quantity_cotton_update = RawMaterialQuantities.objects.last()
         #    current_cotton_quantity = quantity_cotton_update.cotton
         #    total_cotton_quantity = current_cotton_quantity + quantity_of_lastest_item
         #    quantity_cotton_addition = RawMaterialQuantities.objects.last()
         #    quantity_cotton_addition.cotton = total_cotton_quantity
         #    quantity_cotton_addition.save()

         # elif lastest_item_supplied == 'sun_flower':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.sun_flower
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.sun_flower = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'fish':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.fish
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.fish = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'layers_premix':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.layers_premix
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.layers_premix = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'general_purpose_premix':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.general_purpose_premix
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.general_purpose_premix = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'shells':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.shells
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.shells = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'meat_boaster':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.meat_boaster
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.meat_boaster = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'egg_boaster':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.egg_boaster
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.egg_boaster = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'pig_concentrate':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.pig_concentrate
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.pig_concentrate = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'soya_bean':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.soya_bean
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.soya_bean = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'calcium':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.calcium
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.calcium = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'brown_salt':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.brown_salt
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.brown_salt = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'animal_salt':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.animal_salt
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.animal_salt = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'common_salt':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.common_salt
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.common_salt = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'coconut':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.coconut
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.coconut = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'wonder_pig':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.wonder_pig
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.wonder_pig = total_quantity
         #    quantity_addition.save()

         # elif lastest_item_supplied == 'big_pig':
         #    quantity_update = RawMaterialQuantities.objects.last()
         #    current_quantity = quantity_update.big_pig
         #    total_quantity = current_quantity + quantity_of_lastest_item
         #    quantity_addition = RawMaterialQuantities.objects.last()
         #    quantity_addition.big_pig = total_quantity
         #    quantity_addition.save()
   elif check_row == 0:
      #create default quantities
      
      #we get the date and then also populate a specific raw_material
      #We need the date , the raw and quantity
      #put the raw_materials in a list
      # default_quantiites = RawMaterialQuantities.objects.create(date = selected_date,maize_bran = 0 ,cotton = 0,
      #                                                          sun_flower = 0, fish = 0 ,
      #                                                          general_purpose_premix = 0,layers_premix = 0,
      #                                                          shells = 0, meat_boaster = 0,egg_boaster=0,calcium = 0,
      #                                                          soya_bean = 0 , brown_salt = 0, animal_salt = 0 , common_salt = 0,
      #                                                          coconut = 0 , pig_concentrate = 0 , wonder_pig = 0 , big_pig =0  )
      #next thing that we need to do is to populate the RawmaterialQuantities table
      #with the initial values
      #get the item inside the raw materials model and then update the row in RMQ model
      #that specific quantity
      #after populating them with initial value , then i will also have to populate that 
      #latest value inside the RMQ table
      lastest_supply = RawMaterial.objects.last()
      #here we are turning this occurance into a dictionary
      #we might want to print the quantity, just for sastisfaction
      #get the quantity from the dictionary 
      quantity_of_supply = lastest_supply.quantity
      #but still i must change the quantity_of_lastest_item into an int for it to
      #work properly
      # so we also get the specific item in the object because we shall use it to select the 
      #row to update 
      item_of_supply = lastest_supply.item
      #use these two variables quantity_of_lastest_item and lastest_item_supplied to update the row
      # the RawMaterialQuantities model
      if item_of_supply == 'maize_bran':
         #get the current values inside the RawMaterialQuantities
         quantity_update              = RawMaterialQuantities.objects.last()
         current_quantity             = quantity_update.maize_bran
         #now add both quantities from the Raw material table and RawMaterialQuantities table
         total_quantity               = current_quantity + quantity_of_supply
         #then now i can update the value inside the RawMaterialQuantites model          
         quantity_addition            = RawMaterialQuantities.objects.last()
         quantity_addition.maize_bran = total_quantity
         quantity_addition.save()

      elif item_of_supply == 'cotton':
         cotton_update           = RawMaterialQuantities.objects.last()
         cotton_quantity         = cotton_update.cotton
         total_cotton_quantity   = cotton_quantity + quantity_of_supply           
         cotton_addition         = RawMaterialQuantities.objects.last()
         cotton_addition.cotton  = total_cotton_quantity
         cotton_addition.save()

      elif item_of_supply == 'sun_flower':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.sun_flower
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.sun_flower  = total_quantity
         addition.save()

      elif item_of_supply == 'fish':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.fish
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.fish  = total_quantity
         addition.save()

      # elif item_of_supply == 'salt':
      #    update           = RawMaterialQuantities.objects.last()
      #    quantity         = update.salt
      #    total_quantity   = quantity + quantity_of_supply           
      #    addition         = RawMaterialQuantities.objects.last()
      #    addition.salt  = total_quantity
      #    addition.save()

      elif item_of_supply == 'layers_premix':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.layers_premix
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.layers_premix  = total_quantity
         addition.save()

      elif item_of_supply == 'general_purpose_premix':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.general_purpose_premix
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.general_purpose_premix  = total_quantity
         addition.save()

      elif item_of_supply == 'shells':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.shells
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.shells = total_quantity
         addition.save()

      elif item_of_supply == 'meat_boaster':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.meat_boaster
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.meat_boaster = total_quantity
         addition.save()

      elif item_of_supply == 'egg_boaster':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.egg_boaster
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.egg_boaster = total_quantity
         addition.save()

      elif item_of_supply == 'calcium':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.calcium
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.calcium = total_quantity
         addition.save()

      elif item_of_supply == 'soya_bean':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.soya_bean
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.soya_bean = total_quantity
         addition.save()

      elif item_of_supply == 'brown_salt':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.brown_salt
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.brown_salt = total_quantity
         addition.save()

      elif item_of_supply == 'animal_salt':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.animal_salt
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.animal_salt = total_quantity
         addition.save()

      elif item_of_supply == 'common_salt':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.common_salt
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.common_salt = total_quantity
         addition.save()

      elif item_of_supply == 'coconut':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.coconut
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.coconut = total_quantity
         addition.save()

      elif item_of_supply == 'pig_concentrate':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.pig_concentrate
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.pig_concentrate = total_quantity
         addition.save()

      elif item_of_supply == 'wonder_pig':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.wonder_pig
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.wonder_pig = total_quantity
         addition.save()

      elif item_of_supply == 'big_pig':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.big_pig
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.big_pig = total_quantity
         addition.save()

def increment_quantities(increment_value,form ):
   if increment_value > 0:
      #get the current quantity of raw material in the RMQ model
      #Get date from the form
      date_of_supply = form.cleaned_data['date']

      #identify the item that we want to update
      item_supplied = form.cleaned_data['item']
      if item_supplied == 'egg_boaster':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         #get amount supplied    
         item_value = amount_of_supply.egg_boaster
         #add the two together
         incremented_value = item_value + increment_value
         #update the value 
         amount_of_supply.egg_boaster = incremented_value
         amount_of_supply.save()                 
         # then also add the incremented value on the last instance
         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")
         #code below is for incase the dates are not the same.
         if rear_date != earlist_date:
            current_egg_boaster_value = current_supply.egg_boaster
            increased_value = current_egg_boaster_value + increment_value
            current_supply.egg_boaster = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'maize_bran':
         #update the RMQ maize_bran quantity
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.maize_bran
         incremented_value = item_value + increment_value
         amount_of_supply.maize_bran = incremented_value
         amount_of_supply.save()

         #update the last instance
         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_maize_bran_value = current_supply.maize_bran
            increased_value =  current_maize_bran_value + increment_value
            current_supply.maize_bran = increased_value
            current_supply.save()
         else:
            print("move on with life")                      

      elif item_supplied == 'cotton':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.cotton
         incremented_value = item_value + increment_value
         amount_of_supply.cotton = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_cotton_value = current_supply.cotton
            increased_value =  current_cotton_value + increment_value
            current_supply.cotton = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'sun_flower':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.sun_flower
         incremented_value = item_value + increment_value
         amount_of_supply.sun_flower = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_sun_flower_value = current_supply.sun_flower
            increased_value =  current_sun_flower_value + increment_value
            current_supply.sun_flower = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'fish':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.fish
         incremented_value = item_value + increment_value
         amount_of_supply.fish = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_fish_value = current_supply.fish
            increased_value =  current_fish_value + increment_value
            current_supply.fish = increased_value
            current_supply.save()
         else:
            print("move on with life")

      # elif item_supplied == 'salt':
      #    amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      #    item_value = amount_of_supply.salt
      #    incremented_value = item_value + increment_value
      #    amount_of_supply.salt = incremented_value
      #    amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_salt_value = current_supply.salt
            increased_value =  current_salt_value + increment_value
            current_supply.salt = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'layers_premix':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.layers_premix
         incremented_value = item_value + increment_value
         amount_of_supply.layers_premix = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_layers_premix_value = current_supply.layers_premix
            increased_value =  current_layers_premix_value + increment_value
            current_supply.layers_premix = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'general_purpose_premix':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.general_purpose_premix
         incremented_value = item_value + increment_value
         amount_of_supply.general_purpose_premix = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_general_purpose_premix_value = current_supply.general_purpose_premix
            increased_value =  current_general_purpose_premix_value + increment_value
            current_supply.general_purpose_premix = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'shells':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.shells
         incremented_value = item_value + increment_value
         amount_of_supply.shells = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_general_purpose_premix_value = current_supply.shells
            increased_value =  current_shells_value + increment_value
            current_supply.shells = increased_value
            current_supply.save()
         else:
            print("move on with life")
                        
      elif item_supplied == 'meat_boaster':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.meat_boaster
         incremented_value = item_value + increment_value
         amount_of_supply.meat_boaster = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_general_purpose_premix_value = current_supply.meat_boaster
            increased_value =  current_shells_value + increment_value
            current_supply.meat_boaster = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'calcium':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.calcium
         incremented_value = item_value + increment_value
         amount_of_supply.calcium = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_calcium_value = current_supply.calcium
            increased_value =  current_calcium_value + increment_value
            current_supply.calcium = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'soya_bean':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.soya_bean
         incremented_value = item_value + increment_value
         amount_of_supply.soya_bean = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_soya_bean_value = current_supply.soya_bean
            increased_value =  current_soya_bean_value + increment_value
            current_supply.soya_bean = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'brown_salt':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.brown_salt
         incremented_value = item_value + increment_value
         amount_of_supply.brown_salt = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_brown_salt_value = current_supply.brown_salt
            increased_value =  current_brown_salt_value + increment_value
            current_supply.brown_salt = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'animal_salt':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.animal_salt
         incremented_value = item_value + increment_value
         amount_of_supply.animal_salt = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_soya_bean_value = current_supply.animal_salt
            increased_value =  current_soya_bean_value + increment_value
            current_supply.animal_salt = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'common_salt':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.common_salt
         incremented_value = item_value + increment_value
         amount_of_supply.common_salt = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_common_salt_value = current_supply.common_salt
            increased_value =  current_common_salt_value + increment_value
            current_supply.common_salt = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'coconut':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.coconut
         incremented_value = item_value + increment_value
         amount_of_supply.coconut = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_coconut_value = current_supply.coconut
            increased_value =  current_coconut_value + increment_value
            current_supply.coconut = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'pig_concentrate':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.pig_concentrate
         incremented_value = item_value + increment_value
         amount_of_supply.coconut = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_pig_concentrate_value = current_supply.pig_concentrate
            increased_value =  current_pig_concentrate_value + increment_value
            current_supply.pig_concentrate = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'wonder_pig':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.wonder_pig
         incremented_value = item_value + increment_value
         amount_of_supply.wonder_pig = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_wonder_pig_value = current_supply.wonder_pig
            increased_value =  current_wonder_pig_value + increment_value
            current_supply.animal_salt = increased_value
            current_supply.save()
         else:
            print("move on with life")

      elif item_supplied == 'big_pig':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.big_pig
         incremented_value = item_value + increment_value
         amount_of_supply.big_pig = incremented_value
         amount_of_supply.save()

         current_supply = RawMaterialQuantities.objects.last()
         #latest_instance
         #first check if the updated instance the lastest instance are
         #of the same date or not
         last_date = amount_of_supply.date
         rear_date = last_date.strftime("%x")
         current_date = current_supply.date
         earlist_date = current_date.strftime("%x")

         if rear_date != earlist_date:
            current_big_pig_value = current_supply.big_pig
            increased_value =  current_big_pig_value + increment_value
            current_supply.big_pig = increased_value
            current_supply.save()
         else:
            print("move on with life")

def decrement_quantities(decrement_value , form):
   date_of_supply = form.cleaned_data['date']
   #identify the item that we want to update
   item_supplied = form.cleaned_data['item']
   if item_supplied == 'egg_boaster':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      #get amount supplied    
      item_value = amount_of_supply.egg_boaster
      #add the two together
      incremented_value = item_value - decrement_value
      #update the value 
      amount_of_supply.egg_boaster = incremented_value
      amount_of_supply.save()                 
      # then also add the incremented value on the last instance
      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")
      #code below is for incase the dates are not the same.
      if rear_date != earlist_date:
         current_egg_boaster_value = current_supply.egg_boaster
         increased_value = current_egg_boaster_value - decrement_value
         current_supply.egg_boaster = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'maize_bran':
      #update the RMQ maize_bran quantity
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.maize_bran
      incremented_value = item_value - decrement_value
      amount_of_supply.maize_bran = incremented_value
      amount_of_supply.save()

      #update the last instance
      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_maize_bran_value = current_supply.maize_bran
         increased_value =  current_maize_bran_value + decrement_value
         current_supply.maize_bran = increased_value
         current_supply.save()
      else:
         print("move on with life")      

   elif item_supplied == 'cotton':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.cotton
      incremented_value = item_value - decrement_value
      amount_of_supply.cotton = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_cotton_value = current_supply.cotton
         increased_value =  current_cotton_value - decrement_value
         current_supply.cotton = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'sun_flower':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.sun_flower
      incremented_value = item_value - decrement_value
      amount_of_supply.sun_flower = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_sun_flower_value = current_supply.sun_flower
         increased_value =  current_sun_flower_value - decrement_value
         current_supply.sun_flower = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'fish':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.fish
      incremented_value = item_value - decrement_value
      amount_of_supply.fish = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_fish_value = current_supply.fish
         increased_value =  current_fish_value - decrement_value
         current_supply.fish = increased_value
         current_supply.save()
      else:
         print("move on with life")

   # elif item_supplied == 'salt':
   #    amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
   #    item_value = amount_of_supply.salt
   #    incremented_value = item_value - decrement_value
   #    amount_of_supply.salt = incremented_value
   #    amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_salt_value = current_supply.salt
         increased_value =  current_salt_value - decrement_value
         current_supply.salt = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'layers_premix':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.layers_premix
      incremented_value = item_value - decrement_value
      amount_of_supply.layers_premix = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_layers_premix_value = current_supply.layers_premix
         increased_value =  current_layers_premix_value - decrement_value
         current_supply.layers_premix = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'general_purpose_premix':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.general_purpose_premix
      incremented_value = item_value - decrement_value
      amount_of_supply.general_purpose_premix = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_general_purpose_premix_value = current_supply.general_purpose_premix
         increased_value =  current_general_purpose_premix_value - increment_value
         current_supply.general_purpose_premix = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'shells':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.shells
      incremented_value = item_value - decrement_value
      amount_of_supply.shells = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_general_purpose_premix_value = current_supply.shells
         increased_value =  current_shells_value - decrement_value
         current_supply.shells = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'meat_boaster':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.meat_boaster
      incremented_value = item_value - decrement_value
      amount_of_supply.meat_boaster = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_meat_boaster_value = current_supply.meat_boaster
         increased_value =  current_meat_boaster_value - decrement_value
         current_supply.meat_boaster = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'calcium':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.calcium
      incremented_value = item_value - decrement_value
      amount_of_supply.calcium = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_calcium_value = current_supply.calcium
         increased_value =  current_calcium_value - decrement_value
         current_supply.calcium = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'soya_bean':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.soya_bean
      incremented_value = item_value - decrement_value
      amount_of_supply.soya_bean = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_soya_bean_value = current_supply.soya_bean
         increased_value =  current_soya_bean_value - decrement_value
         current_supply.soya_bean = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'brown_salt':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.brown_salt
      incremented_value = item_value - decrement_value
      amount_of_supply.brown_salt = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_brown_salt_value = current_supply.soya_bean
         increased_value =  current_brown_salt_value - decrement_value
         current_supply.brown_salt = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'animal_salt':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.animal_salt
      incremented_value = item_value - decrement_value
      amount_of_supply.animal_salt = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_animal_salt_value = current_supply.animal_salt
         increased_value =  current_animal_salt_value - decrement_value
         current_supply.animal_salt = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'common_salt':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.common_salt
      incremented_value = item_value - decrement_value
      amount_of_supply.common_salt = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_common_salt_value = current_supply.common_salt
         increased_value =  current_common_salt_value - decrement_value
         current_supply.common_salt = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'coconut':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.coconut
      incremented_value = item_value - decrement_value
      amount_of_supply.coconut = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_coconut_value = current_supply.coconut
         increased_value =  current_coconut_value - decrement_value
         current_supply.coconut = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'pig_concentrate':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.pig_concentrate
      incremented_value = item_value - decrement_value
      amount_of_supply.pig_concentrate = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_pig_concentrate_value = current_supply.pig_concentrate
         increased_value =  current_pig_concentrate_value - decrement_value
         current_supply.coconut = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'wonder_pig':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.wonder_pig
      incremented_value = item_value - decrement_value
      amount_of_supply.wonder_pig = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_wonder_pig_value = current_supply.wonder_pig
         increased_value =  current_wonder_pig_value - decrement_value
         current_supply.wonder_pig = increased_value
         current_supply.save()
      else:
         print("move on with life")

   elif item_supplied == 'big_pig':
      amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
      item_value = amount_of_supply.big_pig
      incremented_value = item_value - decrement_value
      amount_of_supply.big_pig = incremented_value
      amount_of_supply.save()

      current_supply = RawMaterialQuantities.objects.last()
      #latest_instance
      #first check if the updated instance the lastest instance are
      #of the same date or not
      last_date = amount_of_supply.date
      rear_date = last_date.strftime("%x")
      current_date = current_supply.date
      earlist_date = current_date.strftime("%x")

      if rear_date != earlist_date:
         current_big_pig_value = current_supply.big_pig
         increased_value =  current_big_pig_value - decrement_value
         current_supply.big_pig = increased_value
         current_supply.save()
      else:
         print("move on with life")

def reduce_due_to_deletion(supply_item,supply_quantity):
   # maize_bran,cotton,sun_flower,fish,salt,general_purpose_premix,layers_premix ,shells 
   # ,meat_boaster ,egg_boaster 
   if supply_item == "maize_bran":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.maize_bran
      quantity_update = current_quantity - supply_quantity
      instance.maize_bran = quantity_update
      instance.save()

   elif supply_item == "cotton":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.cotton
      quantity_update = current_quantity - supply_quantity
      instance.cotton = quantity_update
      instance.save()

   elif supply_item == "sun_flower":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.sun_flower
      quantity_update = current_quantity - supply_quantity
      instance.sun_flower = quantity_update
      instance.save()

   elif supply_item == "fish":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.fish
      quantity_update = current_quantity - supply_quantity
      instance.fish = quantity_update
      instance.save()

   # elif supply_item == "salt":
   #    instance = RawMaterialQuantities.objects.last()
   #    current_quantity = instance.salt
   #    quantity_update = current_quantity - supply_quantity
   #    instance.salt = quantity_update
   #    instance.save()

   elif supply_item == "general_purpose_premix":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.general_purpose_premix
      quantity_update = current_quantity - supply_quantity
      instance.general_purpose_premix = quantity_update
      instance.save()

   elif supply_item == "layers_premix":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.layers_premix
      quantity_update = current_quantity - supply_quantity
      instance.layers_premix = quantity_update
      instance.save()

   elif supply_item == "shells":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.shells
      quantity_update = current_quantity - supply_quantity
      instance.shells = quantity_update
      instance.save()

   elif supply_item == "meat_boaster":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.meat_boaster
      quantity_update = current_quantity - supply_quantity
      instance.meat_boaster = quantity_update
      instance.save()

   elif supply_item == "egg_boaster":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.egg_boaster
      quantity_update = current_quantity - supply_quantity
      instance.egg_boaster = quantity_update
      instance.save()

   elif supply_item == "calcium":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.calcium
      quantity_update = current_quantity - supply_quantity
      instance.calcium = quantity_update
      instance.save()

   elif supply_item == "soya_bean":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.soya_bean
      quantity_update = current_quantity - supply_quantity
      instance.soya_bean = quantity_update
      instance.save()

   elif supply_item == "brown_salt":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.brown_salt
      quantity_update = current_quantity - supply_quantity
      instance.brown_salt = quantity_update
      instance.save()

   elif supply_item == "animal_salt":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.animal_salt
      quantity_update = current_quantity - supply_quantity
      instance.animal_salt = quantity_update
      instance.save()

   elif supply_item == "common_salt":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.common_salt
      quantity_update = current_quantity - supply_quantity
      instance.common_salt = quantity_update
      instance.save()

   elif supply_item == "coconut":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.coconut
      quantity_update = current_quantity - supply_quantity
      instance.coconut = quantity_update
      instance.save()

   elif supply_item == "pig_concentrate":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.pig_concentrate
      quantity_update = current_quantity - supply_quantity
      instance.pig_concentrate = quantity_update
      instance.save()

   elif supply_item == "wonder_pig":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.wonder_pig
      quantity_update = current_quantity - supply_quantity
      instance.wonder_pig = quantity_update
      instance.save()

   elif supply_item == "big_pig":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.big_pig
      quantity_update = current_quantity - supply_quantity
      instance.big_pig = quantity_update
      instance.save()

   return print("Numbers successfully reduced") 

def subtracting(maize_bran,cotton,sun_flower,fish,general_purpose_premix,layers_premix,shells,meat_boaster,egg_boaster,calcium,soya_bean,animal_salt,common_salt,brown_salt,coconut,pig_concentrate,wonder_pig,big_pig):

   instance = RawMaterialQuantities.objects.last()
   #subtract the current information , maize bran

   #maize_bran
   current_maize = instance.maize_bran - maize_bran
   instance.maize_bran = current_maize
   instance.save()
   #cotton
   current_cotton = instance.cotton - cotton
   instance.cotton = current_cotton
   instance.save()
   #sun_flower
   current_sun_flower = instance.sun_flower - sun_flower
   instance.sun_flower = current_sun_flower
   instance.save()
   #fish
   current_fish = instance.fish - fish
   instance.fish = current_fish
   instance.save()
  
   #general_purpose_premix
   current_general_purpose_premix = instance.general_purpose_premix - general_purpose_premix
   instance.general_purpose_premix = current_general_purpose_premix
   instance.save()

   #layers_premix
   current_layers_premix = instance.layers_premix - layers_premix
   instance.layers_premix = current_layers_premix
   instance.save()
   #shells
   current_shells = instance.shells - shells
   instance.shells = current_shells
   instance.save()

   #meat_boaster
   current_meat_boaster = instance.meat_boaster - meat_boaster
   instance.meat_boaster = current_meat_boaster
   instance.save()

   #egg_boaster
   current_egg_boaster = instance.egg_boaster - egg_boaster
   instance.egg_boaster = current_egg_boaster
   instance.save()

   #calcium
   current_calcium = instance.calcium - calcium
   instance.calcium = current_calcium
   instance.save()

   #soya_bean
   current_soya_bean = instance.soya_bean - soya_bean
   instance.soya_bean = current_soya_bean
   instance.save()

   #animal_salt
   current_animal_salt = instance.animal_salt - animal_salt
   instance.animal_salt = current_animal_salt
   instance.save()

   #common_salt
   current_common_salt = instance.common_salt - common_salt
   instance.common_salt = current_common_salt
   instance.save()

   #brown_salt
   current_brown_salt = instance.brown_salt - brown_salt
   instance.brown_salt = current_brown_salt
   instance.save()

   #coconut
   current_coconut = instance.coconut - coconut
   instance.coconut = current_coconut
   instance.save()

   #pig_concentrate
   current_pig_concentrate = instance.pig_concentrate - pig_concentrate
   instance.pig_concentrate = current_pig_concentrate
   instance.save()

   #wonder_pig
   current_wonder_pig = instance.wonder_pig - wonder_pig
   instance.wonder_pig = current_wonder_pig
   instance.save()

   #big_pig
   current_big_pig = instance.big_pig - big_pig
   instance.big_pig = current_big_pig
   instance.save()

def adding(product,maize_bran,cotton,sun_flower,fish,general_purpose_premix,layers_premix,shells,meat_boaster,egg_boaster,calcium,soya_bean,animal_salt,common_salt,brown_salt,coconut,pig_concentrate,wonder_pig,big_pig):   
   #here we are getting the product from the form
   #we could first add up all the rawmats and have one figure
   total_quantity = maize_bran + cotton + sun_flower + fish  + general_purpose_premix + layers_premix + shells + meat_boaster + egg_boaster + calcium + soya_bean + animal_salt + common_salt + brown_salt + coconut + pig_concentrate + wonder_pig + big_pig
   last_quantity = ProductQuantities.objects.last()
   if product == "broilers_marsh":
      item = last_quantity.broilers_marsh 
      new_quantity = total_quantity + item
      last_quantity.broilers_marsh = new_quantity
      last_quantity.save()

   elif product == "chick_marsh":
      item = last_quantity.chick_marsh
      new_quantity = total_quantity + item
      last_quantity.chick_marsh = new_quantity
      last_quantity.save()

   elif product == "old_pig":
      item = last_quantity.old_pig
      new_quantity = total_quantity + item
      last_quantity.old_pig = new_quantity
      last_quantity.save()

   elif product == "growers_marsh":
      item = last_quantity.growers_marsh
      new_quantity = total_quantity + item
      last_quantity.growers_marsh = new_quantity
      last_quantity.save()

   elif product == "layers_marsh":
      item = last_quantity.layers_marsh
      new_quantity = total_quantity + item
      last_quantity.layers_marsh = new_quantity
      last_quantity.save()

   elif product == "young_pig":
      item = last_quantity.young_pig
      new_quantity = total_quantity + item 
      last_quantity.young_pig = new_quantity
      last_quantity.save()

def product_sales_quantity_deduction(product,quantity):
   #Reduce quantity of the product
   #Quantity of the product being sold must subtracted from product inventory
   #Access the sales quantity of the product
   #Access the product inventory quantity
   #identify the product that is being sold.

   #get the last occurance of product quantity
   #broilers_marsh,chick_marsh,old_pig,growers_marsh,layers_marsh,young_pig 
   last_product_quantity = ProductQuantities.objects.last()
   if product == "broilers_marsh":
      current_quantity = last_product_quantity.broilers_marsh
      new_quantity = current_quantity - quantity
      last_product_quantity.broilers_marsh = new_quantity
      last_product_quantity.save()

   elif product == "chick_marsh":
      current_quantity = last_product_quantity.chick_marsh
      new_quantity = current_quantity - quantity
      last_product_quantity.chick_marsh = new_quantity
      last_product_quantity.save()

   elif product == "old_pig":
      current_quantity = last_product_quantity.old_pig
      new_quantity = current_quantity - quantity
      last_product_quantity.old_pig = new_quantity
      last_product_quantity.save()

   elif product == "growers_marsh":
      current_quantity = last_product_quantity.growers_marsh
      new_quantity = current_quantity - quantity
      last_product_quantity.growers_marsh = new_quantity
      last_product_quantity.save()

   elif product == "layers_marsh":
      current_quantity = last_product_quantity.layers_marsh
      new_quantity = current_quantity - quantity
      last_product_quantity.layers_marsh = new_quantity
      last_product_quantity.save()

   elif product == "young_pig":
      current_quantity = last_product_quantity.young_pig
      new_quantity = current_quantity - quantity
      last_product_quantity.young_pig = new_quantity
      last_product_quantity.save()      

def raw_material_sales_quantity_deduction(raw_material,quantity):
   # maize_bran,cotton,sun_flower,fish,salt,layers_premix,general_purpose_premix
   # ,shells,meat_boaster,meat_boaster,egg_boaster,egg_boaster
   last_raw_material = RawMaterialQuantities.objects.last()
   if raw_material == "maize_bran":
      current_quantity = last_raw_material.maize_bran
      new_quantity = current_quantity - quantity
      last_raw_material.maize_bran = new_quantity
      last_raw_material.save()

   elif raw_material == "general_purpose_premix":
      current_quantity = last_raw_material.general_purpose_premix
      new_quantity = current_quantity - quantity
      last_raw_material.general_purpose_premix = new_quantity
      last_raw_material.save()

   elif raw_material == "shells":
      current_quantity = last_raw_material.shells
      new_quantity = current_quantity - quantity
      last_raw_material.shells = new_quantity
      last_raw_material.save()

   elif raw_material == "meat_boaster":
      current_quantity = last_raw_material.meat_boaster
      new_quantity = current_quantity - quantity
      last_raw_material.meat_boaster = new_quantity
      last_raw_material.save()

   elif raw_material == "egg_boaster":
      current_quantity = last_raw_material.egg_boaster
      new_quantity = current_quantity - quantity
      last_raw_material.egg_boaster = new_quantity
      last_raw_material.save()
      
   elif raw_material == "layers_premix":
      current_quantity = last_raw_material.layers_premix
      new_quantity = current_quantity - quantity
      last_raw_material.layers_premix = new_quantity
      last_raw_material.save()

   elif raw_material == "cotton":
      current_quantity = last_raw_material.cotton
      new_quantity = current_quantity - quantity
      last_raw_material.cotton = new_quantity
      last_raw_material.save()

   elif raw_material == "sun_flower":
      current_quantity = last_raw_material.sun_flower
      new_quantity = current_quantity - quantity
      last_raw_material.sun_flower = new_quantity
      last_raw_material.save()

   elif raw_material == "fish":
      current_quantity = last_raw_material.fish
      new_quantity = current_quantity - quantity
      last_raw_material.fish = new_quantity
      last_raw_material.save()

   # elif raw_material == "salt":
   #    current_quantity = last_raw_material.salt
   #    new_quantity = current_quantity - quantity
   #    last_raw_material.salt = new_quantity
   #    last_raw_material.save()

   elif raw_material == "coconut":
      current_quantity = last_raw_material.coconut
      new_quantity = current_quantity - quantity
      last_raw_material.coconut = new_quantity
      last_raw_material.save()

   elif raw_material == "wonder_pig":
      current_quantity = last_raw_material.wonder_pig
      new_quantity = current_quantity - quantity
      last_raw_material.wonder_pig = new_quantity
      last_raw_material.save()

   elif raw_material == "pig_concentrate":
      current_quantity = last_raw_material.pig_concentrate
      new_quantity = current_quantity - quantity
      last_raw_material.pig_concentrate = new_quantity
      last_raw_material.save()

   elif raw_material == "calcium":
      current_quantity = last_raw_material.calcium
      new_quantity = current_quantity - quantity
      last_raw_material.calcium = new_quantity
      last_raw_material.save()

   elif raw_material == "big_pig":
      current_quantity = last_raw_material.big_pig
      new_quantity = current_quantity - quantity
      last_raw_material.big_pig = new_quantity
      last_raw_material.save()

   elif raw_material == "common_salt":
      current_quantity = last_raw_material.common_salt
      new_quantity = current_quantity - quantity
      last_raw_material.common_salt = new_quantity
      last_raw_material.save()

   elif raw_material == "animal_salt":
      current_quantity = last_raw_material.animal_salt
      new_quantity = current_quantity - quantity
      last_raw_material.animal_salt = new_quantity
      last_raw_material.save()

   elif raw_material == "brown_salt":
      current_quantity = last_raw_material.brown_salt
      new_quantity = current_quantity - quantity
      last_raw_material.brown_salt = new_quantity
      last_raw_material.save()

   elif raw_material == "soya_bean":
      current_quantity = last_raw_material.soya_bean
      new_quantity = current_quantity - quantity
      last_raw_material.soya_bean = new_quantity
      last_raw_material.save()

def check_if_product_quantities_are_empty():   

   product_quantity = ProductQuantities.objects.count()
   if product_quantity == 0:
      default_product_quantities = ProductQuantities.objects.create(  
                                                                     date=datetime.datetime.now()
                                                                     ,broilers_marsh = 0
                                                                     ,chick_marsh = 0
                                                                     ,old_pig = 0
                                                                     ,growers_marsh = 0
                                                                     ,layers_marsh = 0
                                                                     ,young_pig = 0

                                                                  )

def check_if_raw_material_quantities_are_empty():

   raw_material_quantity = RawMaterialQuantities.objects.count()
   if raw_material_quantity == 0:
      default_raw_material_quantities = RawMaterialQuantities.objects.create(

                                                                           
                                                                           maize_bran = 0
                                                                           ,cotton = 0
                                                                           ,sun_flower = 0
                                                                           ,fish = 0
                                                                           
                                                                           ,common_salt = 0
                                                                           ,general_purpose_premix = 0
                                                                           ,layers_premix = 0
                                                                           ,shells = 0
                                                                           ,meat_boaster = 0
                                                                           ,calcium = 0
                                                                           ,soya_bean = 0
                                                                           ,brown_salt = 0
                                                                           ,animal_salt = 0
                                                                           ,pig_concentrate = 0
                                                                           ,coconut = 0
                                                                           ,wonder_pig = 0
                                                                           ,big_pig = 0

                                                                           )

def check_raw_material_availabliity(raw_material):
   items = RawMaterial.objects.filter(item = raw_material)
   return len(items)


def computing_profit_of_raw_materials(raw_material,picked_date):

   # selected_date = request.GET.get(date)
   raw_material_cost_price_list = []

   items = RawMaterial.objects.filter(item = raw_material).filter(date = picked_date)

   if len(items) == 0:
      pass
   else:
      for item in items:
         raw_material_cost_price_list.append(item.unit_price)

      print(raw_material_cost_price_list)
      print(raw_material_cost_price_list[-1])

      #Get the selling price of the raw material
      raw_material_sell_price_list = []

      items = RawMaterialSales.objects.filter(raw_material=raw_material)

      #Again because we want to make purchases but not sales for now
      if len(items) == 0:
         pass
      else:
         for item in items:
            raw_material_sell_price_list.append(item.selling_price)

         print(raw_material_sell_price_list)
         print(raw_material_sell_price_list[-1])

         #Get the quantity of raw material sold
         quantity_sold_list = []
         items = RawMaterialSales.objects.filter(raw_material=raw_material)

         for item in items:
            quantity_sold_list.append(item.quantity)

         print(quantity_sold_list)
         print(quantity_sold_list[-1])


         #profit formulae 
         total_profit = (raw_material_sell_price_list[-1] * quantity_sold_list[-1]) - (raw_material_cost_price_list[-1] * quantity_sold_list[-1])

         print(total_profit)
         print(raw_material)

         return  total_profit
      

def save_raw_material_profits_to_database(dictionary):
   raw_material = RawMaterialProfits.objects.create(date=datetime.datetime.now()
                                    ,maize_bran=dictionary["maize_bran"]
                                    ,cotton=dictionary["cotton"]
                                    ,sun_flower = dictionary["sun_flower"]
                                    ,fish = dictionary['fish']
                                    ,general_purpose_premix = dictionary['general_purpose_premix']
                                    ,layers_premix = dictionary['layers_premix']
                                    ,shells = dictionary['meat_boaster']
                                    ,meat_boaster = dictionary['egg_boaster']
                                    ,egg_boaster = dictionary['egg_boaster']
                                    ,calcium = dictionary['calcium']
                                    ,soya_bean = dictionary['soya_bean']
                                    ,brown_salt = dictionary['soya_bean']
                                    ,animal_salt = dictionary['animal_salt']
                                    ,common_salt = dictionary['common_salt']
                                    ,pig_concentrate = dictionary['pig_concentrate']
                                    ,coconut = dictionary['coconut']
                                    ,wonder_pig = dictionary['wonder_pig']
                                    ,big_pig = dictionary['big_pig'])
        
    
@snoop
def profits_for_raw_materials(selected_date,raw_item):
   # selected_date = request.GET.get('select_date')
    
   # raw_item = request.GET.get('raw_materials')
   standard_date = selected_date.strftime('%Y-%m-%d')
   #however standard date is still a string ,we must change it to a date
   splited_date = standard_date.split('-')
   print(splited_date)
   #Give year , month and date a variable
   year = splited_date[0]
   month = splited_date[1]
   day = splited_date[2]

   #create a python date object
   standard_date = datetime.date(int(year), int(month), int(day))

   print(standard_date) 

   print(standard_date)
   print(raw_item)
   print(type(raw_item))
   # Get the unit price from raw_m sales
   #stop query from running when raw_material is not selected
   if raw_item is None:
      pass
   else:
      # lookup = (Q(date__icontains=selected_date ) and Q(raw_material__icontains=raw_item))
      sales = RawMaterialSales.objects.filter(date = selected_date).filter(raw_material = raw_item)
      
      print(sales)
      #To avoid an error when some views this page with having selected date and raw
      #materials
      if sales.exists():
         
         #Create a list to save the unit_prices
         unit_prices = []
         for sale in sales:
            unit_prices.append(sale.selling_price)

         #get the current unit_price
         current_unit_price = statistics.mean(unit_prices)
         print("unit_prices")
         print(current_unit_price)

         #we look for the quantity that has been sold on a specific date and specific
         #raw material and store the volumes in a list

         sales_volume = []

         for sale in sales:
            sales_volume.append(sale.quantity)

         #the total volume sold that day
         quantity_sold = sum(sales_volume)
         print("Sales Volume")
         print(sales_volume)
         print("quantity_sold")
         print(quantity_sold)
         # Look for the cost price of last purchase of the specific raw_material
         last_purchases = RawMaterial.objects.filter(item=raw_item).filter(date=selected_date).order_by('-date')

         print(len(last_purchases))
         #Get the cost price
         # - Get a list of cost_prices
         #this happens when there is no difference in cost price
         #but what if the cost price changes
         lastest_purchases = RawMaterial.objects.filter(item=raw_item).order_by('-date')
         #if there is only one occurance in the rawMaterial table
         if len(lastest_purchases) == 1:
            normal_cost_price = []
            for purchase in last_purchases:
               normal_cost_price.append(purchase.unit_price)

            #To get the current cost price we pick the last one in the list
            current_cost_price = normal_cost_price[-1]

            profit = (current_unit_price * quantity_sold) - (current_cost_price * quantity_sold)
            #reduce on decimal places
            return round(profit,2)
         else:

            #for the first two queries that appear if there is a difference in cost price 
            #then
            loop = 0
            #an empty list to store the two prices
            cost_prices = []
            for purchase in lastest_purchases:
               cost_prices.append(purchase.unit_price)
               loop + 1
               if loop == 2:
                  break

            last_cost_price = cost_prices[1]
            second_last_cost_price = cost_prices[0]

            
            if int(last_cost_price) != int(second_last_cost_price):
               print("There is a difference in cost price")
               #calculate the profit in a different way
               #old stock
               stock = RawMaterialQuantities.objects.last()
               current_quantity = 0
               for attr , value in vars(stock).items():
                  print(attr, '=', value)
                  
                  if attr == raw_item:
                     print("Its a match")
                     print(value)
                     current_quantity += value
                     break

               new_stock = RawMaterialSales.objects.filter(raw_material=raw_item).order_by('-date').first()
               new_stock = new_stock.quantity

               print(new_stock)
               print(current_quantity)
               old_stock = current_quantity - new_stock
               print(old_stock)
               # profit = (current_unit_price * quantity_sold) - (current_cost_price * quantity_sold)
               # return profit
               #old cost price
               old_cost_price = second_last_cost_price
               old_stock_cost = old_stock * old_cost_price
               new_stock_cost = new_stock * last_cost_price
               stock_cost = old_stock_cost + new_stock_cost
               stock_volume = old_stock + new_stock
               current_cost_price =  stock_cost / stock_volume 

               profit = (current_unit_price * quantity_sold) - (current_cost_price * quantity_sold)
               #reduce on the decimal places
               return round(profit,2)

            else:
               normal_cost_price = []
               for purchase in last_purchases:
                  normal_cost_price.append(purchase.unit_price)

               #To get the current cost price we pick the last one in the list
               current_cost_price = normal_cost_price[-1]

               profit = (current_unit_price * quantity_sold) - (current_cost_price * quantity_sold)
               #reduce on decimal places
               return round(profit,2)
                  
          
      else:
         pass
         

