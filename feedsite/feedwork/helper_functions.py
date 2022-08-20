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