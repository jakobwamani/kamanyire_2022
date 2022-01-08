from django.db import models
from decimal import Decimal
# Create your models here.
# declare a new model with a name "GeeksModel"
class RawMaterial(models.Model):

	# fields of the model
	# date,receiptnumber,supplier,item,unit,quantity,amount
	date = models.DateField()
	receipt_number = models.CharField(max_length = 100)
	supplier = models.CharField(max_length = 100)
	#defining the choices
	item = models.CharField(max_length = 50)
	# models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	quantity = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	unit_price = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	#Am making this a null True because when the user is entering the supply data , am not able to make it appear
	#immediately , that's above my paygrade
	# amount = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	transport = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	onloading = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	offloading = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	grinding = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	#Am making this a null True because when the user is entering the supply data , am not able to make it appear
	#immediately , that's above my paygrade
	cost_of_supply = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	# pricing = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	# renames the instances of the model
	# with their title name
	def __str__(self):
		   
		return '{}'.format(self.date)

class Product(models.Model):
	date = models.DateField()
	product = models.CharField(max_length = 100)
	maize_bran = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	cotton = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	sun_flower = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	salt = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	layers_premix = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	shells = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	meat_boaster = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	egg_boaster = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	fish = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	general_purpose_premix = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	def __str__(self):
		return '{}'.format(self.product)

class RawMaterialQuantities(models.Model):
	date = models.DateField()
	maize_bran = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	cotton = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	sun_flower = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	fish = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	salt = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	common_salt = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	general_purpose_premix = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	layers_premix = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	shells = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	meat_boaster = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	egg_boaster = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	calcium = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	soya_bean = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	brown_salt = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	animal_salt = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	pig_concentrate = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	coconut = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	wonder_pig = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	big_pig = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)

	def __str__(self):
		return '{}'.format(self.date)

class ProductQuantities(models.Model):
	date = models.DateField()
	broilers_marsh = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	chick_marsh = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	old_pig = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	growers_marsh = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	layers_marsh = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	young_pig = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	
	def __str__(self):
		return '{}'.format(self.date)

class ProductPrices(models.Model):
	date = models.DateField()
	broilers_marsh = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	chick_marsh = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	old_pig = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	growers_marsh = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	layers_marsh = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	young_pig = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	
	def __str__(self):
		return '{}'.format(self.date)

class RawMaterialPrices(models.Model):
	date = models.DateField()
	maize_bran = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	cotton = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	sun_flower = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	fish = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	salt = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	general_purpose_premix = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	layers_premix = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	shells = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	meat_boaster = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	egg_boaster = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)

	def __str__(self):
		return '{}'.format(self.date)

class ProductSales(models.Model):
	date = models.DateField()
	product = models.CharField(max_length = 50)
	quantity = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	selling_price = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	total = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)

	def __str__(self):
		return '{}'.format(self.date)

class RawMaterialSales(models.Model):
	date = models.DateField()
	raw_material = models.CharField(max_length = 50)
	quantity = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	selling_price = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	total = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)

	def __str__(self):
		return '{}'.format(self.date)