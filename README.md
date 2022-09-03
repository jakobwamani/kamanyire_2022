# kamanyire_2022
Accounting System for a Poultry and Animal Feeds Business

#### User Story 
- A client goes to Mbarara district in Uganda buys 1000kg of maize bran at 1000 ugx per kilo gram 

- Once the 1000kg reach Hoima in Uganda the client is charged a fee of 50,000ugx for transport

- Then also off loading the client is charged 4000ugx for 1000 kilograms

- Then the client adds up the total cost of bringing the maize bran to his shop.

#### Calculation 

Purchase = 1000kgs of maizebran * 1000ugx = 1,000,000ugx 

Transportation expenses = 50,000ugx + 4000ugx

What is the cost of bringing maize bran from Mbarara district to Hoima district is 
1,000,000ugx + 50,000ugx + 4000ugx = 1,054,000ugx

What is the cost of kilogram of maize bran from Mbarara?
1,054,000 ugx / 1000 kgs = 1054 ugx 


total profit = unit price * quantity - unit cost * quantity


After getting the profit of maize bran now we can get the profit of all other raw materials and 
then save them by the date that he can select as we pleases.
fatal: Authentication failed for 

###### Cost price is derived using a method below
If a new purchase of a specified raw material has been made on that day 

Then we get the quantity of the specified raw material before the new purhase had been made

Multiply it by the cost price of the last purchase of a specified raw material before a new purhase been made.

Then Get the quantity of the specified raw material of the new purchase

Multiply it with the new cost price 

Add the two multiplications together and divide it by total quantity of the specified raw material
#### Personal Access Tokens for this project
September 3rd 2022
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

August 30th 2022
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

August 23rd 2022 Kamanyire Version 3
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

August 16th 2022
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

July 30th 2022
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
July 23rd 2022
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

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

January 14th 2021
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
###### January 6th 2022

##### Requirements to install
- Python
- Django
- Python Virtual Environment
- django-calculation

##### Resources
- Making simple calculations in django forms [Calculations in Django forms](https://github.com/blasferna/django-calculation)

- Django documentation [Django Knowledge](https://www.djangoproject.com/)

- Auto Calculations [Auto Calculation in html using javaScript](https://www.youtube.com/watch?v=1UAORTlaqLg&t=269s)

##### Creating project in Django
```shell
django-admin startproject feedsite
```
##### Running the development server
Just to make sure there are no issues run the command below
```shell
python manage.py runserver
```

##### Confirmation Development Server is okay
![DevServer is Okay!](/home/jay/code/kamanyire_2022/docs/devserver.png "DevelopmentServerOkay")

##### Creating the app
Now that we have set up the environment , then let's start creating the app
To create your app, make sure you’re in the same directory as manage.py and type this command:
```shell
python manage.py startapp feedwork
```
##### Writing our first view 
Opening the file feedwork/views.py and put the following Python code in it:
```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the STS Poultry Business ")
```

#### Calling the view
To call the view, we need to map it to a URL - and for this we need a URLconf.

To create a URLconf in the feedwork directory, create a file called urls.py. 

In the feedwork/urls.py file we are including the following code:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

The next step is to point the root URLconf at the feedwork.urls module. In feedsite/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list, so you have:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('feedwork/', include('feedwork.urls')),
    path('admin/', admin.site.urls),
]
```
#### Activating default django models
```shell
 python manage.py migrate
```
This activates default apps listed in the app's list , they need at least one model to work

#### Creating models
This is done inside the feedwork/models.py

#### Activating models
To include the app in our project, we need to add a reference to its configuration class in the INSTALLED_APPS setting. The FeedworkConfig class is in the feedwork/apps.py file, so its dotted path is 'feedwork.apps.FeedworkConfig'. Edit the mysite/settings.py file and add that dotted path to the INSTALLED_APPS setting

Now Django knows to include the feedwork app. Let’s run another command:
```shell
python manage.py makemigrations feedwork
```

#### Creating a super user
```shell
python manage.py createsuperuser
```

#### Make the poll app modifiable in the admin
Only one more thing to do: we need to tell the admin that models have an admin interface. To do this, open the feedwork/admin.py file,
```python
from django.contrib import admin

from feedwork.models import *

admin.site.register(Question)
```
##### January 8th 2021

#### Creating a template system
- First, is to create a directory called templates in our feedwork directory
- Within the templates directory you have just created, create another directory called feedwork, and within that create a file called index.html. 
- In other words, your template should be at feedwork/templates/feedwork/index.html. Because of how the app_directories template loader works as described above, you can refer to this template within Django as feedwork/index.html.

#### Managing static files (e.g. images, JavaScript, CSS)
Am doing this for the dashboard 

- Make sure that django.contrib.staticfiles is included in your INSTALLED_APPS.

- In your settings file, define STATIC_URL, for example:

```python
STATIC_URL = 'static/'
```

#### Models
- Quantites could be integers or decimals

#### Forms
- Quantites could be integers or decimals

#### Supply module

#### Mixture module

#### Expenses module
I have decided to leave the expenses module

#### Raspberry pi
https://raspberrypi.stackexchange.com/questions/30144/connect-raspberry-pi-to-pc-ubuntu-with-ethernet

https://forums.raspberrypi.com/viewtopic.php?t=149681


https://forums.raspberrypi.com/viewtopic.php?t=288769

#### How to make calculations in html
https://www.youtube.com/watch?v=v5pNyxmtp9g


#### Deployment plan
-Django Application running on Start up
-Command to run on Start up
-Django application must be present
-Python 3.8.10 must be present

-i uninstalled Mozilla Firefox on Clients Computer
-i reinstalled it
-i installed python to client's computer on C:\Users\user\AppData\Local\Programs\Python\Python38
-i installed all python libraries that i might need for the Django application to work
-i now installed Git. to C:\Program Files\Git
-Pull the django application into the computer using Git.

### PATs
March 16 2022
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

April 30 2022
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
### March 22nd 2022
Rendering Django Forms Manually
https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html

https://www.geeksforgeeks.org/render-django-form-fields-manually/


https://stackoverflow.com/questions/51936217/arithmetic-operations-between-django-fields-belonging-to-the-same-class-model-i


https://pypi.org/project/django-mathfilters/

https://stackoverflow.com/questions/420703/how-do-i-add-multiple-arguments-to-my-custom-template-filter-in-a-django-templat


https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches


# stock balance of particular raw_material by date

## amount_of_purchases_of_raw_material_by_a_particular_date

### get the date the first raw_material purchase was sold

```python
first_purchase = purchases.objects.filter(raw_material_name__raw_material_name = 'maize_bran').first()
#get the date the the raw material was first purchased
start_date = first_purchase.date
```
*The is a specific way on how to get data from related tables*
[How to deal with One To Many Relationships](https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/)

### get the purchases that have been made since that date up to the selected date

```python

purchases = purchases.objects.filter(raw_material_name__raw_material_name = 'maize_bran').filter(date__range=['2022-08-17', '2022-08-19'])
purchases_list = []
for purchase in purchases:
    puchases_list.append(purchase.quantity)
quantity_of_purchases = sum(purchases_list)
```

## amount_of_sales of a particular raw material by a particular date
#get the date the first raw_material_was sold
```python
first_sale = raw_material_transactions.objects.filter(raw_material_name__raw_material_name = 'maize_bran').first()

```

### get the sales of that particular raw material that have been sold since that date up to the selected date
```python
sales = raw_material_sales.objects.filter(raw_material_name='specified_raw_material').filter(date__range=first_purchase.date,'specified_date')

sales_list = []
for sale in sales:
    sales_list.append(sale.quantity)
quantity_of_sales = sum(sales_list)
```
## amount_raw_material_that_has_been_used_to_make_products_till a particular_date
0. get to know one product where the raw material is involved
```python
    products = raw_material_separations.objects.filter(product_name__product_name='layers marsh')
    # the above query will be get us many instances but shall select the last one for instance 
    products = raw_material_separations.objects.filter(product_name__product_name='layers marsh').last()
    products.product_name.product_name
```
1. get the standard weight of a particular product
```python
    standard_weight_list = []
    weights = raw_material_separations.objects.filter(product_name='one_product.product_name.product_name')
    for weight in weights:
        standard_weight_list.append(weight.ratio)

    standard_weight = sum(standard_weight_list)
```
2. understand how much of the raw material can be separated in the standard weight of a particular_product
```python
    module_weight = raw_material_separations.objects.filter(product_name__product_name='layers marsh').filter(raw_material_name__raw_material_name = 'maize_bran')
    #get the weight
    standard_weight_of_raw_material = weights.ratio
```
3. understand how much raw_material can be separated in one kilogram of a particular product
```python
    
    #how about one kilo of the standard weight
    one_kilogram_of_standard_weight = standard_weight / standard_weight_of_raw_material
```
5. get the total number of kilograms that has been mixed for a particular product till a particular date.
```python

raw_material_quantity = []

#get the first product mixture

product_quantity = products.objects.filter(product_name__product_name='layers marsh').first()

start_date = product_quantity.date
 

#get the different product mixtures done till a particular date
product_quantities = products.objects.filter(product_name__product_name='layers marsh').filter(date__range='first_date','specified_date')

for product in product_quantities:
    raw_material_quantity.append(product_quantities.quantity)

quantity_of_product_mixed = sum(raw_material_quantity)
```
5. understand how much raw_material can be mixed in the total number of kilograms for a particular product that has been mixed till a particular date.
```python
total_weight_of_raw_material_mixed = one_kilogram_of_standard_weight * quantity_of_product_mixed
```
6. Stock Balance
```python
stock balance = quantity_of_purchases - quantity_of_sales - total_weight_of_raw_material_mixed
```
7. Scale
***If we have been able to do it for one product then we can do it for other products and then add together the stock balances***



### Basic formula
***stock balance = amount of purchases of raw material by a particular date - amount of raw material sales by a particular date - amount raw material used to make products by a paticular date
***


# Stock balance for a particular product by a particular date

1. Get date of the first mixture of a particular product
```python
    out_come = products.objects.filter(product_name__product_name='layers marsh').first()
    start_date = out_come.date
```
2. Get amount of the product that had been mixture till a particular date
```python
    product_quantity_list = []
    out_comes = products.objects.filter(date__range='start_date','specified_date')
    for product in products:
        product_quantity_list.append(product.quantity)
    product_quantity_summation = sum(product_quantity_list)
```
4. Get date of the first sale of a particular product
```python
    product = product_sales.objects.filter(product_name='specified_product_name').first()
    start_date = product.date
```
5. Get amount of the product that had been sold till a particular date
```python
    product_sale_list = []
    sales = product_sales.objects.filter(date__range='start_date','specified_date')
    for sale in sales:
        product_sale_list.append(sale.quantity)
    product_sale_summation = sum(product_sale_list)
```
6. Compute the formula

### Basic formula
***stock balance = amount_of_product_that_has_been_mixed by a particular date - amount of product that has been sold by a particular date***

# cost price of a particular raw material by date
1. Get the unit price of a particular raw material in its last purchase
```python
new_purchase = purchases.objects.filter(raw_material_name='specified_raw_material').filter(date='date').last()

new_unit_price = new_purchase.unit_price
```
2. Get the quantity of the a particular raw material in its last purchase
```python
new_quantity = new_purchase.quantity
```
3. Get the logistics of that a particular raw material in its last purchase
```python
    new_logistics = new.objects.filter(purchase='last_purchase.id').filter(date='date')
    new_loading = new_logistics.loading
    new_off_loading = new_logistics.offloading
    new_transport = new_logistics.transport

    # Add the logistics together
    logistics = new_loading + new_off_loading + new_transport
```
4. To get the new cost price we multiply the unit price by the quantity and then lastly add the logistics
```python
new_total_cost = (new_unit_price * new_quantity) + logistics
```
5. Divide the addition above by the quantity of the raw material that was purchased 
```python
new_cost_price = new_total_cost / new_quantity
```
6. Check to see if there is a difference in the unit price from the second last purchase of a particular raw material
```python 
purchases = purchases.objects.filter(raw_material_name='specified_raw_material').filter(date='date')

if len(purchases) > 1:

    loop = 0
    for purchase in purchases
        loop += 1
        if loop == 1:
            #get date of the current occurance of purchases
            old_date = purchases.date
            #get the unit price of the current occurance of purchases
            old_unit_price = purchases.unit_price
            #then we compare the old unit price and the new unit price
            #then compare the unit prices
            if old_unit_price == new_unit_price:
                pass 
            else:
                


            break
elif len(purchases) == 0:

    #get the date the first purchase was made
    purchases = purchases.objects.filter(raw_material_name='specified_raw_material').first()
    #to get the last date
    last_purchases = purchases.objects.filter(raw_material_name='specified_raw_material').filter().last()
    last_purchases.date 

    first_date = purchases.date

    range_stuff = purchases.objects.filter(raw_material_name='specified_raw_material').filter(date__range=[first_date,last_purchases.date])

    loop = 0
    for row in range_stuff:
        loop += 1
        if loop == 1:
            old_date = range_stuff.date 

            old_unit_price = range_stuff.unit_price 

            if old_unit_price == new_unit_price:
                pass 
            else:
                
```
7. if there is a difference , then we calculate the stock balance of that particular raw material till a particular date.
```python
#we use a function that we have used above
```
8. To get the old_total_cost we multiply the stock balance with the unit price of the raw material in its second last purchase

9. To get the old_cost_price we divide the old_total_cost by the stock balance  

10. To find the optimal cost price we get the  mean of the between the old cost price and new cost price.

# cost price of a particular a product by date
1. Select a particular product in a product sale on a particular date
```python
result_name = product_names.objects.filter(product_name='broilers marsh')

```
2. Find out the raw materials that are involved in that product
```python
#one begins by know how the product has been seperated
separations = raw_material_separations.objects.filter(product_name='specified_product_name')
names = []
for separation in separations:
    names.append(separation.raw_material_name)
#understand to which raw material do those separation names belong
#by removing any duplicate
names = list(dict.fromkeys(names))
print(names)
```
3. Find the cost prices of the different raw materials involved in that product
```python
#the cost price of each and every raw material found in that names list
cost_price_dict = {}
for name in names:
    #use the above function to find the cost price by a specific date
```
4. Find the standard weight of the product
```python
separations = raw_material_separations.objects.filter(product_name='specified_product_name')
ratios = {}
standard_weight = 0
for separation in separations:
    ratios[separation.raw_material_name]=separation.ratio
for key, value in ratios.items()
    standard_weight += value
```
5. Divide those cost prices by the specific ratios involved in the standard weight of a product
```python
    divided_cost_price_dict = {}
    for raw_material, cost_price in cost_price_dict.items()
        for raw_material_separation , ratio in ratios.items()
            divided_cost_price_dict[raw_material] = cost_price/ratio
```
6. Findout the cost prices involved in one kilogram of the product
```python
standard_cost_price = 0 
for key , value in divided_cost_price_dict.items()
    standard_cost_price += value

standard_weight = standard_cost_price

one_kilogram_of_standard_weight = standard_weight/standard_cost_price 
```

7. Mulitply that with the quantity of the product that has been sold till a particular date.
```python

    #Get date of the first sale of a particular product

    product = product_sales.objects.filter(product_name='specified_product_name').first()
    start_date = product.date

    #Get amount of the product that had been sold till a particular date
    product_sale_list = []
    sales = product_sales.objects.filter(date__range='start_date','specified_date')
    for sale in sales:
        product_sale_list.append(sale.quantity)
    product_sale_summation = sum(product_sale_list)


    cost_price = one_kilogram_of_standard_weight * product_sale_summation
```

# profit of a particular raw material by date
1. Get the unit price of the raw material sale on a specific date
```python
sales = raw_material_transactions.objects.filter(raw_material_name__raw_material_name='maize_bran').filter(date='2022-08-21')

for sale in sales:
    #get the unit price
    sale.unit_price
```
2. Get the quantity of the raw material sale on a specific date
```python
#get the quantity
    sale.quantity
```
3. Get the cost price of the raw material on a specific date
```python
    #get the cost price of raw material using the above defined function
```
4. Do the basic formula below and get the profit
```python
    #do this with a the basic profit formula below
    #do the above steps for every occurance and then add the profits 
```
***profit = (unit_price_of_raw_material_sale * quantity_of_raw_material_sale) - (cost_price_of_raw_material * quantity_of_raw_material_sale)***


# profit of a particular product by date
1. Get the unit price of the product sale on a specific date
```python
sales = product_sales.objects.filter(product_name__product_name='layers marsh').filter(date='2022-08-21')

for sale in sales:
    #get the unit_price
    sale.unit_price
```
2. Get the quantity of the product sale on a specific date
```python
    #get the quantity
    sale.quantity
```
3. Get the cost price of the product on a specific date
```python
    #get the cost price of the product using the above defined function
```
4. Do the basic formula below and get the profit
```python
    #do this with a the basic profit formula below
    #do the above steps for every occurance and then add the profits 
```
***profit = (unit_price_of_product_sale * quantity_of_product_sale) - (cost_price_of_product * quantity_of_product_sale)***


# Models

1. advance payments
2. employment terms
3. expense names
4. logistics
5. product sales
6. purchases
7. raw material names
8. raw material sales
9. suppliers 
10. employee 
11. product sales 
12. salary 
13. product 
14. 


# Cost price of a product

there are 100kg of maize bran in the standard weight of the layers-mash-with-coconut

How about one kilogram of the standard weight of the layers-mash-with-coconut

how about the the quantity of the product that has been mixed

basic quantity of an involved raw material * cost price of one kilogram

addition of the cost prices

division of the addition by the quantity of the product that has been mixed

virtual environment of python anywhere
/home/yakobo/.virtualenvs/tangibleai