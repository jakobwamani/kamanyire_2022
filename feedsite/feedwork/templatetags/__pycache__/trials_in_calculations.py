from feedwork.models import *


result_name = product_names.objects.filter(product_name='Layers-mash-with-coconut')

   if result_name == None:

      pass

   else:
      # Find out the raw materials that are involved in that product

      separations = raw_material_separations.objects.filter(product_name__product_name='Layers-mash-with-coconut')

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

      separations = raw_material_separations.objects.filter(product_name__product_name='Layers-mash-with-coconut')

      ratios = {}

      for separation in separations:

         ratios[separation.raw_material_name.raw_material_name]=separation.ratio

      print(ratios)

      for key, value in ratios.items():

         standard_weight += value

      print(standard_weight)



      divided_weights = {}

      for key , value in ratios:

         standard_weight = value

         #How about one kilogram of standard weight

         one_kilogram_of_standard_weight = value / standard_weight

         #append the divided weights dictionary

         divided_weights[key] = one_kilogram_of_standard_weight


      #how about when the weights have increased

      #we can get the weights of different raw materials in a product

      mix = products.objects.filter(product_name__product_name='Layers-mash-with-coconut').first()

      if mix == None:

         total_mixes = 0

         return total_mixes

      else:

         start_date = sale.date

         #Get amount of the product that had been sold till a particular date

         mixes = products.objects.filter(date__range=[picked_date,start_date])

         product_sale_list = []

         if mixes == None:

            total_mixes = 0

         else:


            for mixing in mixes:

               product_sale_list.append(mixing.quantity)

               print(mixing.quantity)

            print(picked_date)

            print(start_date)

            print(product_sale_list)

            total_mixes = sum(product_sale_list)

   
      # how about when the weights have increased

      actual_weights = {}

      for key, value in divided_weights:

         actual_weights[key] = value * total_mixes
        

     

      

