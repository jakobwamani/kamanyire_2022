from feedwork.models import *




standard_weight  = raw_material_separations.objects.filter(product_name__product_name='Layers-mash-with-coconut').aggregate(Sum('ratio'))['ratio__sum']

print(standard_weight)

 standard_weight_fit  = raw_material_separations.objects.filter(product_name__product_name='Layers-mash-with-coconut').get(raw_material_name__raw_material_name='Maize-bran').ratio

print(standard_weight_fit)

#now find out how much of the layers-mash-with-coconut has been mixed

mixture_weight = products.objects.filter(product_name__product_name='Layers-mash-with-coconut').aggregate(Sum('quantity'))['quantity__sum']

print(mixture_weight)

mixed_amount = (standard_weight_fit/standard_weight) * mixture_weight


def stock_balance_for_raw_materials(picked_date,basic_input):

   first_purchase = purchases.objects.filter(raw_material_name__raw_material_name = basic_input).first()

   if first_purchase == None:

      quantity_of_purchases = 0 

      first_sale = raw_material_transactions.objects.filter(raw_material_name__raw_material_name = basic_input).first()

      if first_sale == None:

         quantity_of_sales = 0 

      else:

         start_date = first_sale.date

         sales = raw_material_transactions.objects.filter(raw_material_name__raw_material_name = basic_input).filter(date__range=[start_date,picked_date]).aggregate(Sum('quantity'))['quantity__sum']

         quantity_of_sales = sales


      results = product_names.objects.all()

      if len(results_list) == 0:

         stock_balance = quantity_of_purchases - quantity_of_sales

         print("stock_balance",stock_balance)

         return stock_balance

      else:

         total_amount_of_mixed_amounts = []

         sum_of_mixed_amounts = sum(total_amount_of_mixed_amounts)

         for result in results:

            standard_weight  = raw_material_separations.objects.filter(product_name__product_name=result.product_name).aggregate(Sum('ratio'))['ratio__sum']

            standard_weight_fit  = raw_material_separations.objects.filter(product_name__product_name=result.product_name).get(raw_material_name__raw_material_name=basic_input).ratio

            #now find out how much of the layers-mash-with-coconut has been mixed

            mixture_weight = products.objects.filter(product_name__product_name=result.product_name).aggregate(Sum('quantity'))['quantity__sum']

            mixed_amount = (standard_weight_fit/standard_weight) * mixture_weight

            total_amount_of_mixed_amounts.append(mixed_amount)

         # stock Balance

         stock_balance = quantity_of_purchases - quantity_of_sales - 

         print("stock_balance",stock_balance)

         return stock_balance

