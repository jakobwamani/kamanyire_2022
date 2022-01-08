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