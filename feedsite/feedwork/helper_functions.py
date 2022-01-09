from feedwork.models import *
import datetime

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
         #we want to get the lastest value of a specific item
         #We just look through the RawMaterial model and look for last input of a specific item
         # get_lastest_item_supplied = RawMaterial.objects.latest('-item')
         get_lastest_item_supplied = RawMaterial.objects.last()
         quantity_of_lastest_item  = get_lastest_item_supplied.quantity
         lastest_item_supplied     = get_lastest_item_supplied.item
         #use these two variables quantity_of_lastest_item and lastest_item_supplied to update the row
         # the RawMaterialQuantities model
         if lastest_item_supplied == 'maize_bran':
            #get the current values inside the RawMaterialQuantities
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.maize_bran
            #now add both quantities from the Raw material table and RawMaterialQuantities table
            total_quantity = current_quantity + quantity_of_lastest_item
            #then now i can update the value inside the RawMaterialQuantites model       
            # #i proceed to update the RMQ table
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.maize_bran = total_quantity
            quantity_addition.save() 

         elif lastest_item_supplied == 'cotton':
            quantity_cotton_update = RawMaterialQuantities.objects.last()
            current_cotton_quantity = quantity_cotton_update.cotton
            total_cotton_quantity = current_cotton_quantity + quantity_of_lastest_item
            quantity_cotton_addition = RawMaterialQuantities.objects.last()
            quantity_cotton_addition.cotton = total_cotton_quantity
            quantity_cotton_addition.save()

         elif lastest_item_supplied == 'sun_flower':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.sun_flower
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.sun_flower = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'fish':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.fish
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.fish = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'salt':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.salt
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.salt = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'layers_premix':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.layers_premix
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.layers_premix = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'general_purpose_premix':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.general_purpose_premix
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.general_purpose_premix = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'shells':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.shells
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.shells = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'meat_boaster':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.meat_boaster
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.meat_boaster = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'egg_boaster':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.egg_boaster
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.egg_boaster = total_quantity
            quantity_addition.save()

         elif lastest_item_supplied == 'pig_concentrate':
            quantity_update = RawMaterialQuantities.objects.last()
            current_quantity = quantity_update.pig_concentrate
            total_quantity = current_quantity + quantity_of_lastest_item
            quantity_addition = RawMaterialQuantities.objects.last()
            quantity_addition.pig_concentrate = total_quantity
            quantity_addition.save()

   elif check_row == 0:
      #create default quantities
     
      default_quantiites = RawMaterialQuantities.objects.create(date = datetime.datetime.now(),maize_bran = 0 ,cotton = 0,
                                                               sun_flower = 0, fish = 0,salt = 0 ,
                                                               general_purpose_premix = 0,layers_premix = 0,
                                                               shells = 0, meat_boaster = 0,egg_boaster=0,calcium = 0,
                                                               soya_bean = 0 , brown_salt = 0, animal_salt = 0 , common_salt = 0,
                                                               coconut = 0 , pig_concentrate = 0 , wonder_pig = 0 , big_pig =0  )
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

      elif item_of_supply == 'salt':
         update           = RawMaterialQuantities.objects.last()
         quantity         = update.salt
         total_quantity   = quantity + quantity_of_supply           
         addition         = RawMaterialQuantities.objects.last()
         addition.salt  = total_quantity
         addition.save()

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

def update_quantites(increment_value,decrement_value , form ):
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

      elif item_supplied == 'salt':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.salt
         incremented_value = item_value + increment_value
         amount_of_supply.salt = incremented_value
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

   else:
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

      elif item_supplied == 'salt':
         amount_of_supply = RawMaterialQuantities.objects.get(date=date_of_supply)
         item_value = amount_of_supply.salt
         incremented_value = item_value - decrement_value
         amount_of_supply.salt = incremented_value
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
            current_general_purpose_premix_value = current_supply.meat_boaster
            increased_value =  current_shells_value - decrement_value
            current_supply.meat_boaster = increased_value
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

   elif supply_item == "salt":
      instance = RawMaterialQuantities.objects.last()
      current_quantity = instance.salt
      quantity_update = current_quantity - supply_quantity
      instance.salt = quantity_update
      instance.save()

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

   return print("Numbers successfully reduced")