from django.db import models
from decimal import Decimal
from django.utils import timezone

from datetimewidget.widgets import DateTimeWidget
import datetime
# Create your models here.
# declare a new model with a name "GeeksModel"
class RawMaterial(models.Model):

	# fields of the model
	# date,receiptnumber,supplier,item,unit,quantity,amount
	date = models.DateField()
	time = models.TimeField()
	receipt_number = models.CharField(max_length = 100)
	supplier = models.CharField(max_length = 100)
	#defining the choices
	item = models.CharField(max_length = 50)
	# models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	quantity = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	unit_price = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	#Am making this a null True because when the user is entering the supply data , am not able to make it appear
	total = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	
	def __str__(self):
		   
		return '{}'.format(self.date)

class Product(models.Model):
	date = models.DateTimeField()
	product = models.CharField(max_length = 100)
	maize_bran = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	cotton = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	sun_flower = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	layers_premix = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	shells = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	meat_boaster = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	egg_boaster = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	fish = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	general_purpose_premix = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	calcium = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	soya_bean = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	brown_salt = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	animal_salt = models.DecimalField(max_digits=10 , decimal_places=3 ,default=0.0)
	common_salt = models.DecimalField(max_digits=10 , decimal_places=3 ,default=0.0)
	brown_salt = models.DecimalField(max_digits=10 , decimal_places=3 ,default=0.0)
	coconut = models.DecimalField(max_digits=10 , decimal_places=3 ,default=0.0)
	pig_concentrate = models.DecimalField(max_digits=10 , decimal_places=3 ,default=0.0)
	wonder_pig = models.DecimalField(max_digits=10 , decimal_places=3 , default=0.0)
	big_pig	= models.DecimalField(max_digits=10 , decimal_places=3 ,default=0.0)
	def __str__(self):
		return '{}'.format(self.date)

class RawMaterialQuantities(models.Model):
	date = models.DateField(default=datetime.date.today)
	time = models.TimeField(default=timezone.now())
	maize_bran = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0 , null=True)
	cotton = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	sun_flower = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	fish = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	common_salt = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	general_purpose_premix = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	layers_premix = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	shells = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	meat_boaster = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	egg_boaster = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	calcium = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	soya_bean = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	brown_salt = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	animal_salt = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	pig_concentrate = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	coconut = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	wonder_pig = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	big_pig = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)

	def __str__(self):
		return '{}'.format(self.date)

class ProductQuantities(models.Model):
	date = models.DateField(default=datetime.date.today)
	time = models.TimeField(default=timezone.now())
	broilers_marsh = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	chick_marsh = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	pig_marsh = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	growers_marsh = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	layers_marsh = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	
	
	def __str__(self):
		return '{}'.format(self.date)

class ProductPrices(models.Model):
	date = models.DateTimeField()
	broilers_marsh = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	chick_marsh = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	
	growers_marsh = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	layers_marsh = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	pig_marsh = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	
	def __str__(self):
		return '{}'.format(self.date)

class RawMaterialPrices(models.Model):
	date = models.DateTimeField()
	maize_bran = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	cotton = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	sun_flower = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	fish = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	
	general_purpose_premix = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	layers_premix = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	shells = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	meat_boaster = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	egg_boaster = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	calcium = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	soya_bean = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	brown_salt = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	animal_salt = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	common_salt = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	pig_concentrate = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	coconut = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	wonder_pig = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	big_pig = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)

	def __str__(self):
		return '{}'.format(self.date)

class ProductSales(models.Model):
	date = models.DateTimeField()
	product = models.CharField(max_length = 50)
	quantity = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	selling_price = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	total = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)

	def __str__(self):
		return '{}'.format(self.date)

class RawMaterialSales(models.Model):
	date = models.DateField()
	time = models.TimeField()
	raw_material = models.CharField(max_length = 50)
	quantity = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	selling_price = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	total = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)

	def __str__(self):
		return '{}'.format(self.date)

class Expenses(models.Model):
	date = models.DateTimeField()
	expense = models.CharField(max_length = 50)
	supplier = models.CharField(max_length= 50)
	unit = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	quantity = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	rate = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0)
	amount = models.DecimalField(max_digits = 10 , decimal_places=3 , default = 0.0)
	def __str__(self):
		return '{}'.format(self.date)	
      
class RawMaterialProfits(models.Model):
	date = models.DateTimeField()
	maize_bran = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0 , null=True)
	cotton = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	sun_flower = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0 , null=True)
	fish = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0, null=True)
	general_purpose_premix = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0,null=True)
	layers_premix = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0,null=True)
	shells = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0,null=True)
	meat_boaster = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0,null=True)
	egg_boaster = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0,null=True)
	calcium = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0,null=True)
	soya_bean = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0,null=True)
	brown_salt = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0,null=True)
	animal_salt = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0,null=True)
	common_salt = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0,null=True)
	pig_concentrate = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0,null=True)
	coconut = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0,null=True)
	wonder_pig = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0,null=True)
	big_pig = models.DecimalField(max_digits=10, decimal_places=3 , default=0.0,null=True)

	def __str__(self):
		return '{}'.format(self.date)




	
