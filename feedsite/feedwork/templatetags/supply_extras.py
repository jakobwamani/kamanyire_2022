from django import template

from requests import request
from feedwork.models import *
from feedwork.urls import *
import datetime
from django.db.models import Q
# Import statistics Library
import statistics
import snoop
from django.utils import timezone
from decimal import Decimal
import datetime





register = template.Library()

@register.filter

def work_on_amount(value,args):
	print(args)
	# since we can be able to grab the query object this side , then we can use it the way we want too

	# the amount by multiplying the unit_price and the quantity
	amount = args.unit_price * args.quantity

	return amount

@register.filter
def work_on_the_full_amount(value,args):
	#first thing is to get the amount
	amount = args.unit_price * args.quantity


	#is equal to amount + transport + onloading + offloading + grinding
	fullamount = amount + args.transport + args.onloading + args.offloading + args.grinding


	return fullamount

@register.simple_tag
def multiple_ops(loading,off_loading,transport,quantity,unit_price):
   #do your stuff
   cost_of_purchase = (loading+off_loading+transport)+(quantity*unit_price)
   return cost_of_purchase


def check_if_query_exists(x,y):
   try:

      standard_weight_fit  = raw_material_separations.objects.filter(product_name__product_name=x).get(raw_material_name__raw_material_name=y).ratio

      return standard_weight_fit

   except ObjectDoesNotExist:

      standard_weight_fit = 0 

      return standard_weight_fit
@snoop
def stock_balance_for_raw_materials(picked_date,basic_input):
   # stock balance of particular raw_material by date

   ## we get to know how much of raw_material has been purchased till a particular_date

   ## We begin by getting the date the we first purchased that specific raw material
   date_of_first_purchase = purchases.objects.filter(raw_material_name__raw_material_name = basic_input).first()
   # first_purchase = purchases.objects.filter(raw_material_name__raw_material_name = basic_input).first()

   if date_of_first_purchase == None:
      pass
   else:

      purchase_quantity = purchases.objects.filter(raw_material_name__raw_material_name = basic_input).filter(date__range=[date_of_first_purchase.date,picked_date]).aggregate(Sum('quantity'))['quantity__sum']

      if purchase_quantity == None:

         purchase_quantity = 0 

      else:

         # amount_of_sales of a particular raw material by a particular date

         ### get the date the first raw_material_was sold

         date_of_the_first_sale = raw_material_transactions.objects.filter(raw_material_name__raw_material_name = basic_input).first()

         if date_of_the_first_sale == None:
            pass
         else:
         ### get the sales of that particular raw material that have been sold since that date up to the selected date
         
            print(date_of_the_first_sale.date)


            sales_quantity = raw_material_transactions.objects.filter(raw_material_name__raw_material_name = basic_input).filter(date__range=[date_of_the_first_sale.date,picked_date]).aggregate(Sum('quantity'))['quantity__sum']

            # ## amount_raw_material_that_has_been_used_to_make_products_till a particular_date

            # ### how when we do all the products
            results = product_names.objects.all()

            total_amount_of_mixed_amounts = []

            

            if len(results) == 0:

               stock_balance = purchase_quantity - sales_quantity

               print("stock_balance",stock_balance)

               return stock_balance

            else:

               

               for result in results:

                  standard_weight  = raw_material_separations.objects.filter(product_name__product_name=result.product_name).aggregate(Sum('ratio'))['ratio__sum']

                  standard_weight_fit = check_if_query_exists(result.product_name,basic_input)

                  mixture_weight = products.objects.filter(product_name__product_name=result.product_name).aggregate(Sum('quantity'))['quantity__sum']

                  if mixture_weight == None:

                     mixture_weight = 0 

                     mixed_amount = (standard_weight_fit/standard_weight) * mixture_weight

                     total_amount_of_mixed_amounts.append(int(mixed_amount))

                  else:

                     mixed_amount = (standard_weight_fit/standard_weight) * mixture_weight

                     total_amount_of_mixed_amounts.append(int(mixed_amount))


            # stock Balance
            print(purchase_quantity)

            print(sales_quantity)

            print(sum(total_amount_of_mixed_amounts))

            stock_balance = purchase_quantity - sales_quantity - sum(total_amount_of_mixed_amounts)

            print("stock_balance",stock_balance)

            return stock_balance


def x_stock_balance_for_raw_materials(picked_date,basic_input):
   # stock balance of particular raw_material by date

   ## we get to know how much of raw_material has been purchased till a particular_date

   ## We begin by getting the date the we first purchased that specific raw material
   first_purchase = purchases.objects.filter(raw_material_name__raw_material_name = basic_input).first()

   if first_purchase == None:

      quantity_of_purchases = 0 
      
      ## amount_of_sales of a particular raw material by a particular date

      ### get the date the first raw_material_was sold

      first_sale = raw_material_transactions.objects.filter(raw_material_name__raw_material_name = basic_input).first()

      if first_sale == None:
         
         quantity_of_sales = 0 

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

      if len(results_list) == 0:

         stock_balance = quantity_of_purchases - quantity_of_sales

         print("stock_balance",stock_balance)

         return stock_balance

      else:

         for result in results:
            ### start by one product where the raw material is involved

            out_come_names = raw_material_separations.objects.filter(product_name__product_name=result.product_name)

            # the above query will be get us many instances but shall select the last one for instance 

            out_come_name = raw_material_separations.objects.filter(product_name__product_name=result.product_name).last()

            if out_come_name == None:
               
               stock_balance = quantity_of_purchases - quantity_of_sales

               print("stock_balance",stock_balance)

               return stock_balance

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

         quantity_of_sales = 0 

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

      if len(results_list) == 0:

         stock_balance = quantity_of_purchases - quantity_of_sales

         print("stock_balance",stock_balance)

         return stock_balance

      for result in results:
         ### start by one product where the raw material is involved

         out_come_names = raw_material_separations.objects.filter(product_name__product_name=result)

         # the above query will be get us many instances but shall select the last one for instance 

         out_come_name = raw_material_separations.objects.filter(product_name__product_name=result).last()

         if out_come_name == None:
            
            stock_balance = quantity_of_purchases - quantity_of_sales

            print("stock_balance",stock_balance)

            return stock_balance

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

@register.filter
@snoop
def cost_price_of_raw_material(picked_date,basic_input):
   
   ## cost price of a particular raw material by date
   ## Get the unit price of a particular raw material in its last purchase
   new_purchase = purchases.objects.filter(raw_material_name__raw_material_name=basic_input).filter(date=picked_date).last()

   ## Get the quantity of the a particular raw material in its last purchase
   if new_purchase == None:
     new_unit_price = Decimal('0')
     new_cost_price = Decimal('0')
   else:

      #now_get_the_direct_expenses_first
      new_direct_expenses = direct_expenses.objects.filter(purchase__id=new_purchase.id)

      direct_expenses_list = []

      for expense in new_direct_expenses:

         expense_summation = expense.unit_price * expense.quantity

         direct_expenses_list.append(expense_summation)

      total_direct_expenses = sum(direct_expenses_list)

      
      if new_direct_expenses == None:
         
         total_direct_expenses = 0 

      else:

         total_direct_expenses = int(total_direct_expenses)

         #then work on the purchase
         new_unit_price = new_purchase.unit_price

         ## Get the quantity of the a particular raw material in its last purchase

         new_quantity = new_purchase.quantity

         ## Get the logistics of that a particular raw material in its last purchase
         new_logistics = logistics.objects.filter(purchase__id=new_purchase.id).last()

         if new_logistics == None:
            total_cost_price = (new_unit_price * new_quantity) + total_direct_expenses

            new_cost_price = total_cost_price / new_quantity

            return new_cost_price

         else:
            new_loading = new_logistics.loading

            new_off_loading = new_logistics.off_loading

            new_transport = new_logistics.transport

            # Add the logistics together

            movement_costs = new_loading + new_off_loading + new_transport

            ## To get the new cost price we multiply the unit price by the quantity and then lastly add the logistics

            new_total_cost = (new_unit_price * new_quantity) + movement_costs + total_direct_expenses

            ## Divide the addition above by the quantity of the raw material that was purchased 

            new_cost_price = new_total_cost / new_quantity

            return new_cost_price



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

   if sale == None:

      stock_balance = product_quantity_mixed -  0 

      return stock_balance

   else: 

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


@register.filter
@snoop
def cost_price_of_raw_material_with_no_date(basic_input):
   
   ## cost price of a particular raw material by date
   ## Get the unit price of a particular raw material in its last purchase
   new_purchase = purchases.objects.filter(raw_material_name__raw_material_name=basic_input).last()

   ## Get the quantity of the a particular raw material in its last purchase
   if new_purchase == None:
     new_unit_price = Decimal('0')
     new_cost_price = Decimal('0')
   else:

      #now_get_the_direct_expenses_first
      new_direct_expenses = direct_expenses.objects.filter(purchase__id=new_purchase.id)

      direct_expenses_list = []

      for expense in new_direct_expenses:

         expense_summation = expense.unit_price * expense.quantity

         direct_expenses_list.append(expense_summation)

      total_direct_expenses = sum(direct_expenses_list)

      
      if new_direct_expenses == None:
         
         total_direct_expenses = 0 

      else:

         total_direct_expenses = int(total_direct_expenses)

         #then work on the purchase
         new_unit_price = new_purchase.unit_price

         ## Get the quantity of the a particular raw material in its last purchase

         new_quantity = new_purchase.quantity

         ## Get the logistics of that a particular raw material in its last purchase
         new_logistics = logistics.objects.filter(purchase__id=new_purchase.id).last()

         if new_logistics == None:
            total_cost_price = (new_unit_price * new_quantity) + total_direct_expenses

            new_cost_price = total_cost_price / new_quantity

            return new_cost_price

         else:
            new_loading = new_logistics.loading

            new_off_loading = new_logistics.off_loading

            new_transport = new_logistics.transport

            # Add the logistics together

            movement_costs = new_loading + new_off_loading + new_transport

            ## To get the new cost price we multiply the unit price by the quantity and then lastly add the logistics

            new_total_cost = (new_unit_price * new_quantity) + movement_costs + total_direct_expenses

            ## Divide the addition above by the quantity of the raw material that was purchased 

            new_cost_price = new_total_cost / new_quantity

            return new_cost_price



@register.filter
@snoop
def cost_price_of_product(picked_date,out_come):

   result_name = product_names.objects.filter(product_name=out_come)

   if result_name == None:

      pass

   else:
	   # Find out the raw materials that are involved in that product

      separations = raw_material_separations.objects.filter(product_name__product_name=out_come)

      names = {}

      for separation in separations:

         names[separation.separation_name]=separation.raw_material_name.raw_material_name

	   # understand to which raw material do those separation names belong

      print(names)


	   # Find the cost prices of the different raw materials involved in that product

      cost_price_dict = {}

      for key , value in names.items():

         cost_price_dict[value]=cost_price_of_raw_material_with_no_date(value)

      print(cost_price_dict)


      #Find the weights of different raw material in the product 
	   #Find the standard weight of the product
      #Get the amount that has been sold 

      separations = raw_material_separations.objects.filter(product_name__product_name=out_come)

      ratios = {}

      standard_weight = 0

      standard_cost = 0

      for separation in separations:

         ratios[separation.raw_material_name.raw_material_name]=separation.ratio

      for key, value in ratios.items():

         standard_weight += value

         for raw_material_name , cost_of_one_kg in cost_price_dict.items():

            if key == raw_material_name:

               if cost_of_one_kg == None:

                  cost_of_one_kg = 0 

                  standard_cost += cost_of_one_kg          

               else:

                  standard_cost += (cost_of_one_kg * value )

      print(standard_weight)

      print(ratios)

      ## Standard cost

      
      print(standard_cost)

      cost_price = standard_cost / standard_weight

      return cost_price



