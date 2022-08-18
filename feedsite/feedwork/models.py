from django.db import models
from decimal import Decimal
from django.utils import timezone
from datetimewidget.widgets import DateTimeWidget
import datetime

class raw_materials(models.Model):
	date = models.DateField()
	time = models.TimeField()
	raw_material_name = models.CharField(max_length=50)
		
	def __str__(self):		   
		return ' {}'.format(self.raw_material_name)

class suppliers(models.Model):
	date = models.DateField()
	time = models.TimeField()
	supplier_name = models.CharField(max_length=50)
		
	def __str__(self):		   
		return '{}'.format(self.supplier_name)

class purchases(models.Model):
	raw_material_name = models.ForeignKey(raw_materials, on_delete=models.CASCADE)
	supplier = models.ForeignKey(suppliers, on_delete=models.CASCADE)
	# logistics = models.ForeignKey(logistics, on_delete=models.CASCADE)
	date = models.DateField()
	time = models.TimeField()
	unit_price = models.IntegerField()
	quantity = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)

	def __str__(self):
		return 'Purchase id: {} :Purchase Date: {} :Purchase Time: {} : Raw Material: {} : Supplier: {} : Unit Price: {} : Quantity: {}'.format(self.id,self.date,self.time,self.raw_material_name,self.supplier,self.unit_price,self.quantity)

class logistics(models.Model):
	purchase = models.ForeignKey(purchases,on_delete=models.CASCADE)
	date = models.DateField()
	time = models.TimeField()
	loading = models.IntegerField()
	off_loading = models.IntegerField()
	transport = models.IntegerField()

	def __str__(self):		   
		return ' {} : {} : {}'.format(self.date,self.time,self.purchase)


	
class raw_material_transactions(models.Model):
	raw_material_name = models.ForeignKey(raw_materials, on_delete=models.CASCADE)
	date = models.DateField()
	time = models.TimeField()
	unit_price = models.IntegerField()
	quantity = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	
	def __str__(self):
		return 'id : {} : Date : {} : Time : {}  Raw Material : {}'.format(self.id,self.date,self.time,self.raw_material_name)


class product_names(models.Model):
	date = models.DateField()
	time = models.TimeField()
	product_name = models.CharField(max_length=50 , )

	def __str__(self):
		return 'id : {} : product_name : {}'.format(self.id,self.product_name)

class products(models.Model):
	product_name = models.ForeignKey(product_names, on_delete=models.CASCADE)
	date = models.DateField()
	time = models.TimeField()
	quantity = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)

	def __str__(self):
		return 'date : {} : product_name : {} : quantity : {}'.format(self.id,self.date,self.product_name,self.quantity)

class raw_material_separations(models.Model):
	raw_material_name = models.ForeignKey(raw_materials, on_delete=models.CASCADE)
	product_name = models.ForeignKey(product_names, on_delete=models.CASCADE)
	date = models.DateField()
	time = models.TimeField()
	separation_name = models.CharField(max_length=50)
	ratio = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)

	def __str__(self):
		return '{} : {} : {} : {} : {}'.format(self.id,self.raw_material_name,self.product_name,self.separation_name,self.ratio)



class product_sales(models.Model):
	product_name = models.ForeignKey(product_names, on_delete=models.CASCADE)
	date = models.DateField()
	time = models.TimeField()
	quantity = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	unit_price = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)
	def __str__(self):
		return '{} : {} : {} : {}'.format(self.id,self.product_name,self.quantity,self.unit_price)

class expense_names(models.Model):
	date = models.DateField()
	time = models.TimeField()
	expense_name = models.CharField(max_length=50)

	def __str__(self):
		return '{} : {}'.format(self.id,self.expense_name)

class expense_units(models.Model):
	date = models.DateField()
	time = models.TimeField()
	unit_name = models.CharField(max_length=50)

	def __str__(self):
		return '{} : {}'.format(self.id,self.unit_name)

class expenses(models.Model):
	expense_name = models.ForeignKey(expense_names, on_delete=models.CASCADE)
	expense_unit = models.ForeignKey(expense_units, on_delete=models.CASCADE)
	date = models.DateField()
	time = models.TimeField()
	quantity = models.DecimalField(max_digits=10, decimal_places=2 , default=0.0)

	def __str__(self):
		return '{} : {} : {}'.format(self.id,self.expense_name,self.quantity)

class employee(models.Model):
	date = models.DateField()
	time = models.TimeField()
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	gender = models.CharField(max_length = 50)
	phone_number_one = models.CharField(max_length = 50)
	phone_number_two = models.CharField(max_length = 50)
	employment_start_date = models.DateField()

	def __str__(self):
		return '{} : {} : {}'.format(self.id,self.first_name,self.last_name)

class employment_terms(models.Model):
	employee_id = models.ForeignKey(employee, on_delete=models.CASCADE)
	date = models.DateField()
	time = models.TimeField()
	agreed_salary = models.IntegerField()
	salary_start_date = models.DateField()
	salary_end_date = models.DateField()

	def __str__(self):
		return '{} : {} : {}'.format(self.id,self.employee_id,self.agreed_salary)

	
class advance_payments(models.Model):
	employee_id = models.ForeignKey(employee, on_delete=models.CASCADE)
	date = models.DateField()
	time = models.TimeField()
	advance = models.IntegerField()
	
	def __str__(self):
		return '{} : {} : {}'.format(self.id,self.employee_id,self.advance)

class salary_payments(models.Model):
	employee_id = models.ForeignKey(employee, on_delete=models.CASCADE)
	date = models.DateField()
	time = models.TimeField()
	salary = models.IntegerField()
	
	def __str__(self):
		return '{} : {} : {}'.format(self.id,self.self.employee_id,self.salary)

	
