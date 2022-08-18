from django import forms
from feedwork.models import *
from django.utils import timezone
# from django.utils import timezone.localtime
# from .widgets import  DateTimePickerInput
from datetimewidget.widgets import DateTimeWidget
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
import calculation
import datetime

#querysets
raw_material_query = raw_materials.objects.all()
logistic_query = logistics.objects.all()
supplier_query = suppliers.objects.all()
product_name_query = product_names.objects.all()
expense_name_query = expense_names.objects.all()
expense_unit_query = expense_units.objects.all()
employee_query = employee.objects.all()
purchase_query = purchases.objects.all()

class raw_material_form(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	raw_material_name = forms.CharField(max_length=50)
		
	class Meta:
		model = raw_materials
		fields = ["date","time","raw_material_name"]

class raw_material_transactions_form(forms.ModelForm):
	raw_material_name = forms.ModelChoiceField(queryset = raw_material_query)
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	unit_price = forms.IntegerField()
	quantity = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	
	class Meta:
		model = raw_material_transactions
		fields = ["date","time","raw_material_name","unit_price","quantity"]

class supplier_form(forms.ModelForm):
	
	supplier_name = forms.CharField(max_length=50)
		
	class Meta:
		model = suppliers
		fields = ["date","time","supplier_name"]

class logistic_form(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	purchase = forms.ModelChoiceField(queryset = purchase_query)
	loading = forms.IntegerField()
	off_loading = forms.IntegerField()
	transport = forms.IntegerField()

	class Meta:
		model = logistics
		fields = ["date","time","purchase","loading","off_loading","transport"]

class purchase_form(forms.ModelForm):
	raw_material_name = forms.ModelChoiceField(queryset = raw_material_query)
	supplier = forms.ModelChoiceField(queryset = supplier_query)
	
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	unit_price = forms.IntegerField()
	quantity = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)

	class Meta:
		model = purchases
		fields = ["date","time","raw_material_name","supplier","unit_price","quantity"]

class raw_material_transaction_form(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	raw_material_name = forms.ModelChoiceField(queryset = raw_material_query)
	unit_price = forms.IntegerField()
	quantity = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	
	class Meta:
		model = raw_material_transactions
		fields = ["date","time","raw_material_name","unit_price","quantity"]

class product_name_form(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	product_name = forms.CharField(max_length=50)

	class Meta:
		model = product_names
		fields = ["date","time","product_name"]

class product_form(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	product_name = forms.ModelChoiceField(queryset = product_name_query)
	quantity = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)

	class Meta:
		model = products
		fields = ["date","time","product_name","quantity"]

class raw_material_separation_form(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	raw_material_name = forms.ModelChoiceField(queryset = raw_material_query)
	product_name = forms.ModelChoiceField(queryset = product_name_query)
	separation_name = forms.CharField(max_length=50)
	ratio = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)

	class Meta:
		model = raw_material_separations
		fields = ["date","time","raw_material_name","product_name","separation_name","ratio"]

class product_sale_form(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	product_name = forms.ModelChoiceField(queryset = product_name_query)
	quantity = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	unit_price = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	class Meta:
		model = product_sales
		fields = ["date","time","product_name","quantity","unit_price"]

class expense_name_form(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	expense_name = forms.CharField(max_length=50)

	class Meta:
		model = expense_names
		fields = ["date","time","expense_name"]

class expense_unit_form(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	unit_name = forms.CharField(max_length=50)

	class Meta:
		fields = ["date","time","unit_name"]

class expense_form(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	expense_name = forms.ModelChoiceField(queryset = expense_name_query)
	expense_unit = forms.ModelChoiceField(queryset = expense_unit_query)
	quantity = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)

	class Meta:
		fields = ["date","time","expense_name","expense_unit","quantity"]

class employee_form(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	gender = forms.CharField(max_length = 50)
	phone_number_one = forms.CharField(max_length = 50)
	phone_number_two = forms.CharField(max_length = 50)
	employment_start_date = forms.DateField()

	class Meta:
		fields = ["date","time","first_name","last_name","gender","phone_number_one","phone_number_two","employment_start_date"]

class employment_term_form(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	employee_id = forms.ModelChoiceField(queryset = employee_query)
	agreed_salary = forms.IntegerField()
	salary_start_date = forms.DateField()
	salary_end_date = forms.DateField()

	class Meta:
		fields = ["date","time","employee_id","agreed_salary","salary_start_date","salary_end_date"]
	
class advance_payment_form(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	employee_id = forms.ModelChoiceField(queryset = employee_query)
	advance = forms.IntegerField()
	
	class Meta:
		fields = ["date","time","employee_id","advance"]

class salary_payment_form(forms.ModelForm):
	employee_id = forms.ModelChoiceField(queryset = employee_query)
	YEARS = [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
	salary = forms.IntegerField()
	
	class Meta:
		fields = ["date","time","employee_id","salary"]
	

