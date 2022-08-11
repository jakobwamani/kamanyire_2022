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


