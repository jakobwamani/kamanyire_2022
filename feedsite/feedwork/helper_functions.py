from requests import request
from feedwork.models import *
import datetime
from django.db.models import Q
# Import statistics Library
import statistics
import snoop
from django.utils import timezone
from decimal import Decimal
import datetime
@snoop

def stock_balance_for_raw_materials(picked_date,basic_input):
   # stock balance of particular raw_material by date

   ## we get to know how much of raw_material has been purchased till a particular_date

   ## We begin by getting the date the we first purchased that specific raw material
   first_purchase = purchases.objects.filter(raw_material_name__raw_material_name = basic_input).first()

   if first_purchase == None:
      pass 
   else:
      #get the date the the raw material was first purchased
      start_date = first_purchase.date

      ### get the amount purchases that have been made since that date up to the selected date
      takes = purchases.objects.filter(raw_material_name__raw_material_name = basic_input).filter(date__range=[start_date, picked_date])

      purchases_list = []

      for purchase in takes:

         purchases_list.append(purchase.quantity)

      quantity_of_purchases = sum(purchases_list)





      ## amount_of_sales of a particular raw material by a particular date

      ### get the date the first raw_material_was sold

      first_sale = raw_material_transactions.objects.filter(raw_material_name__raw_material_name = basic_input).first()

      if first_sale == None:
         pass 
      else:
         ### get the date the raw was first sold
         start_date = first_sale.date

         ### get the sales of that particular raw material that have been sold since that date up to the selected date
         sales = raw_material_transactions.objects.filter(raw_material_name__raw_material_name = basic_input).filter(date__range=[start_date,picked_date])

         sales_list = []

         for sale in sales:

            sales_list.append(sale.quantity)

         quantity_of_sales = sum(sales_list)





      ## amount_raw_material_that_has_been_used_to_make_products_till a particular_date

      ### how when we do all the products
      results = product_names.objects.all()

      results_list = []

      for result in results:
         ### start by one product where the raw material is involved

         out_come_names = raw_material_separations.objects.filter(product_name__product_name=result)

         # the above query will be get us many instances but shall select the last one for instance 

         out_come_name = raw_material_separations.objects.filter(product_name__product_name=result).last()

         if out_come_name == None:
            pass 
         else:
            specified_product = out_come_name.product_name.product_name

            #get the standard weight of a particular product

            standard_weight_list = []

            weights = raw_material_separations.objects.filter(product_name__product_name=specified_product)

            for weight in weights:

               standard_weight_list.append(weight.ratio)

            standard_weight = sum(standard_weight_list)

            ## understand how much of the raw material can be separated in the standard weight of a particular_product

            module_weight = raw_material_separations.objects.filter(product_name__product_name=result).filter(raw_material_name__raw_material_name = basic_input)

            module_weight_list = []

            for weight in module_weight:

               module_weight_list.append(weight.ratio)

            standard_weight_of_raw_material = sum(module_weight_list)

            ## understand how much raw_material can be separated in one kilogram of a particular product

            # one_kilogram_of_standard_weight = standard_weight / standard_weight_of_raw_material
            one_kilogram_of_standard_weight = division(standard_weight,standard_weight_of_raw_material)

            ## get the total number of kilograms that has been mixed for a particular product till a particular date.

            out_come = products.objects.filter(product_name__product_name=result).first()

            start_date = out_come.date

            ## get the different product mixtures done till a particular date

            out_comes = products.objects.filter(product_name__product_name=result).filter(date__range=[start_date,picked_date])

            product_quantities_list = []

            for quantity in out_comes:

               product_quantities_list.append(quantity.quantity)

            quantity_of_product_mixed = sum(product_quantities_list)

            results_list.append(quantity_of_product_mixed)

            total_quantity_of_product_mixed_using_raw_material = sum(results_list)

            ## understand how much raw_material can be mixed in the total number of kilograms for a particular product that has been mixed till a particular date.

            total_weight_of_raw_material_mixed = one_kilogram_of_standard_weight * total_quantity_of_product_mixed_using_raw_material



            # stock Balance

            stock_balance = quantity_of_purchases - quantity_of_sales - total_weight_of_raw_material_mixed

            print("stock_balance",stock_balance)

            return stock_balance


def division(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0




def stock_balance_for_products(product,picked_date):
   # Stock balance for a particular product by a particular date

   ## Get date of the first mixture of a particular product

   out_come = products.objects.filter(product_name__product_name=product).first()

   start_date = out_come.date 

   start_date = start_date.strftime("%Y-%m-%d")

   ## Get amount of the product that had been mixture till a particular date

   product_quantity_list = []

   out_comes = out_comes = products.objects.filter(date__range=[start_date,picked_date])

   for out_come in out_comes:

     product_quantity_list.append(out_come.quantity)

   product_quantity_mixed = sum(product_quantity_list)

   ## Get date of the first sale of a particular product

   sale = product_sales.objects.filter(product_name__product_name=product).first()

   start_date = sale.date

   start_date = start_date.strftime("%Y-%m-%d")

   # Get amount of the product that had been sold till a particular date

   product_sale_list = []

   sales = product_sales.objects.filter(product_name__product_name=product).filter(date__range=[start_date,picked_date])

   for sale in sales:

     product_sale_list.append(sale.quantity)

   total_product_sold = sum(product_sale_list)

   #stock balance
   stock_balance = product_quantity_mixed - total_product_sold

   print(stock_balance)

   return stock_balance






def cost_price_of_raw_material(picked_date,basic_input):
   
   ## cost price of a particular raw material by date
   ## Get the unit price of a particular raw material in its last purchase
   new_purchase = purchases.objects.filter(raw_material_name__raw_material_name=basic_input).filter(date=picked_date).last()

   ## Get the quantity of the a particular raw material in its last purchase
   if new_purchase == None:
     new_unit_price = Decimal('0')
     new_cost_price = Decimal('0')
   else:

      new_unit_price = new_purchase.unit_price

      ## Get the quantity of the a particular raw material in its last purchase

      new_quantity = new_purchase.quantity

      ## Get the logistics of that a particular raw material in its last purchase
      new_logistics = logistics.objects.filter(purchase__id=new_purchase.id).last()

      if new_logistics == None:
         total_cost_price = new_unit_price * new_quantity

         new_cost_price = total_cost_price / new_quantity

      else:
         new_loading = new_logistics.loading

         new_off_loading = new_logistics.off_loading

         new_transport = new_logistics.transport

         # Add the logistics together

         movement_costs = new_loading + new_off_loading + new_transport

         ## To get the new cost price we multiply the unit price by the quantity and then lastly add the logistics

         new_total_cost = (new_unit_price * new_quantity) + movement_costs

         ## Divide the addition above by the quantity of the raw material that was purchased 

         new_cost_price = new_total_cost / new_quantity

   ## Check to see if there is a difference in the unit price from the second last purchase of a particular raw material

   enforcements = purchases.objects.filter(raw_material_name__raw_material_name=basic_input).filter(date=picked_date).order_by('time')

   ## This works if a another purchase was made that day

   if len(enforcements) >= 1:

      loop = 0

      for enforcement in enforcements:

         loop += 1

         if loop == 1:

            #get date of the current occurance of purchases

            old_date = enforcement.date

            #get the unit price of the current occurance of purchases

            old_unit_price = enforcement.unit_price

            #then we compare the old unit price and the new unit price

            #then compare the unit prices

            if old_unit_price == new_unit_price:

               pass 

            else:

               ## if there is a difference , then we calculate the stock balance of that particular raw material till a particular date.

               stock_balance = stock_balance_for_raw_materials(picked_date,basic_input)

               ## To get the old_total_cost we multiply the stock balance with the unit price of the raw material in its second last purchase

               old_total_cost = stock_balance * old_unit_price

               ## To get the old_cost_price we divide the old_total_cost by the stock balance 

               old_cost_price = old_total_cost / stock_balance

               ## To find the optimal cost price we get the  mean of the between the old cost price and new cost price.

               optimal_cost_price = statistics.mean([old_cost_price,new_cost_price])

               return optimal_cost_price

   else:
      ## if a purchase was made the previous days we the date of the first ever purchase 

      first_enforcement = purchases.objects.filter(raw_material_name__raw_material_name=basic_input).first()

      if first_enforcement == None:

         optimal_cost_price = Decimal('0')

         return optimal_cost_price

      else:

         ## first date
         first_date = first_enforcement.date  

         ## Find all the purchases that ever been made from the first purchase to the last selected purchase

         enforcements = purchases.objects.filter(raw_material_name__raw_material_name=basic_input).filter(date__range=[first_date,picked_date])

         loop = 0

         for enforcement in enforcements:

            loop += 1

            if loop == 1:

               old_date = enforcement.date 

               old_unit_price = enforcement.unit_price


               if old_unit_price == new_unit_price:
                  pass 

               else:

                  stock_balance = stock_balance_for_raw_materials(picked_date,basic_input)
                  ## To get the old_total_cost we multiply the stock balance with the unit price of the raw material in its second last purchase

                  old_total_cost = stock_balance * old_unit_price

                  ## To get the old_cost_price we divide the old_total_cost by the stock balance 

                  old_cost_price = old_total_cost / stock_balance

                  ## To find the optimal cost price we get the  mean of the between the old cost price and new cost price.

                  optimal_cost_price = statistics.mean([old_cost_price,new_cost_price])

                  return optimal_cost_price

                     