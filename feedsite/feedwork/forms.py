from django import forms
from feedwork.models import *
from django.utils import timezone
# from django.utils import timezone.localtime
# from .widgets import  DateTimePickerInput
from datetimewidget.widgets import DateTimeWidget
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
import calculation
import datetime

RAW_MATERIAL_CHOICES = (("maize_bran" , "maize bran"),("cotton", "cotton")
,("sun_flower" , "sun flower"),("fish" , "fish"),("calcium" , "calcium"),("soya_bean","soya bean")
,("animal_salt","animal salt"),("common_salt","common salt"),("coconut","coconut"),("pig_concentrate","pig concentrate")
,("wonder_pig","wonder pig"),("big_pig","big pig"),("general_purpose_premix" , "general purpose premix")
,("layers_premix" , "layers premix"),("brown_salt","brown_salt"),("shells" , "shells"),("meat_boaster" , "meat boaster"),("egg_boaster" ,"egg boaster"))
# creating a form

expense_categories = (	("Loading","Loading")
						,("Offloading","Offloading")
						,("Allowance","Allowance")
						,("Overtime_allowance","Overtime_allowance")
						,("Milling","Milling")
						,("Lunch_Allowance","Lunch_Allowance")
						,("Permit_for_Mukene","Permit_for_Mukene")
						,("Frying","Frying")
						,("Sacks","Sacks")
						,("Polyethene_Bag","Polyethene_Bag")
						,("Strings","Strings")
						,("Income_Tax","Income_Tax")
						,("Trading_License","Trading_License")
						,("Property_Tax","Property_Tax")
						,("Electricity","Electricity")
						,("Accounting","Accounting")
					 )
class RawMaterialForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	# date = forms.DateField(widget=forms.SplitDateTimeWidget(),initial=timezone.now())
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	time = forms.TimeField(initial=timezone.now())
    #birth_date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
	receipt_number = forms.DecimalField(initial = 0)
	supplier = forms.CharField()
	item = forms.ChoiceField(choices=RAW_MATERIAL_CHOICES)
	
	quantity = forms.DecimalField(initial = 0.0)
	loading = forms.DecimalField(initial=0.0)
	off_loading = forms.DecimalField(initial=0.0)
	transport = forms.DecimalField(initial=0.0)
	unit_price = forms.DecimalField(initial= 0.0)
	total = forms.DecimalField(initial=0.0)
	# total = forms.DecimalField(
 	#        widget=calculation.FormulaInput('quantity * unit_price') # <- using single math expression
 	#    )
	
	class Meta:
		# specify model to be used
		model = RawMaterial

		# exclude = ["amount","fullamount",]
		fields = ["date","time","receipt_number","supplier","item","quantity","unit_price","loading","off_loading","transport","total"]
		widgets = {
            'date': DateTimePickerInput()
        }



class ExpenseForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
    #birth_date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
	expense = forms.ChoiceField(choices = expense_categories)
	supplier = forms.CharField(max_length= 50)
	unit = forms.DecimalField(max_digits=10, decimal_places=3 , initial=0.0)
	quantity = forms.DecimalField(max_digits=10, decimal_places=3 , initial=0.0)
	rate = forms.DecimalField(max_digits=10, decimal_places=3 , initial=0.0)
	amount = forms.DecimalField(
        widget=calculation.FormulaInput('unit*quantity*rate') )
	
	class Meta:
		# specify model to be used
		model = Expenses
		# exclude = ["amount","fullamount",]
		fields = ["date","expense","supplier","unit","quantity","rate","amount"]

#supply form
class SupplyForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]

	date = forms.DateTimeField(widget=DateTimeWidget)
    #birth_date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
	receipt_number = forms.DecimalField(initial = 0)
	supplier = forms.CharField()
	item = forms.ChoiceField(choices=RAW_MATERIAL_CHOICES)
	# item = forms.CharField()
	quantity = forms.DecimalField(initial = 0.0)
	unit_price = forms.DecimalField(initial = 0.0)
	# i  cannot edit this stuff from right here so all amounts will shown in the retrieve view
	# amount = forms.DecimalField(initial = 0)
	# total = forms.DecimalField( initial = 0.0)
	total = forms.DecimalField(
        widget=calculation.FormulaInput('quantity*unit_price') # <- using single math expression
    )
	# i  cannot edit this stuff from right here so all amounts will shown in the retrieve view
	# fullamount = forms.DecimalField(initial = 0)
	# pricing = forms.DecimalField(help_text='First check to cost of supply to update this')
	# create meta class
	class Meta:
		# specify model to be used
		model = RawMaterial
		# exclude = ["amount","fullamount",]
		fields = ["date","receipt_number","supplier","item","quantity","unit_price","total"]
		widgets = {
            #Use localization and bootstrap 3
            'datetime': DateTimeWidget(attrs={'id':"date"}, usel10n = True, bootstrap_version=3)
        }
# broilers_mash
# brown_salt
# calcium
# chick_mash
# coconut
# cotton_cake
# egg_boaster
# growers_mash
# layers_mash
# lime
# meat_boaster
PRODUCT_CHOICES = (("broilers_marsh","broilers_marsh") 
,("chick_marsh","chick_marsh")
,("growers_marsh","growers_marsh")
,("pig_marsh","pig_marsh")
,("layers_marsh","layers_marsh"))
class ProductForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	# date = forms.DateField()
	product = forms.ChoiceField(choices=PRODUCT_CHOICES)
	maize_bran = forms.DecimalField(initial = 0.0)
	cotton = forms.DecimalField(initial = 0.0)
	sun_flower = forms.DecimalField(initial = 0.0)
	layers_premix = forms.DecimalField(initial = 0.0)
	general_purpose_premix = forms.DecimalField(initial = 0.0)
	shells = forms.DecimalField(initial = 0.0)
	meat_boaster = forms.DecimalField(initial = 0.0)
	egg_boaster = forms.DecimalField(initial = 0.0)
	fish = forms.DecimalField(initial = 0.0)
	calcium = forms.DecimalField(initial = 0.0)
	soya_bean = forms.DecimalField(initial = 0.0)
	animal_salt = forms.DecimalField(initial = 0.0)
	common_salt = forms.DecimalField(initial = 0.0)
	brown_salt = forms.DecimalField(initial = 0.0)
	coconut = forms.DecimalField(initial = 0.0)
	pig_concentrate = forms.DecimalField(initial = 0.0)
	wonder_pig = forms.DecimalField(initial = 0.0)
	big_pig = forms.DecimalField(initial = 0.0)
	
	class Meta:
		model = Product

		fields = ["date","product","maize_bran","cotton","sun_flower","layers_premix","general_purpose_premix","shells","meat_boaster","egg_boaster","fish","calcium","soya_bean","animal_salt","common_salt","brown_salt","coconut","pig_concentrate","wonder_pig","big_pig"]

class ProductPriceForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	broilers_marsh = forms.DecimalField(initial = 0)
	chick_marsh = forms.DecimalField(initial = 0)
	old_pig = forms.DecimalField(initial = 0)
	growers_marsh = forms.DecimalField(initial = 0)
	layers_marsh = forms.DecimalField(initial = 0)
	young_pig = forms.DecimalField(initial = 0)

	class Meta:
		model = ProductPrices

		fields = ["date","broilers_marsh","chick_marsh","old_pig","growers_marsh","layers_marsh","young_pig"]

class RawMaterialPricesForm(forms.ModelForm):
	# quantity_id = models.AutoField(primary_key=True)
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	# date = models.DateField()
	maize_bran = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	cotton = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	sun_flower = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	fish = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	# salt = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	general_purpose_premix = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	layers_premix = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	shells = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	meat_boaster = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	egg_boaster = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	calcium = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	soya_bean = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	brown_salt = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	animal_salt = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	common_salt = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	pig_concentrate = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	coconut = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	wonder_pig = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	big_pig = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)

	class Meta:
		model = RawMaterialPrices

		fields = ["date","maize_bran","cotton","sun_flower","layers_premix","general_purpose_premix","shells","meat_boaster","egg_boaster","fish","calcium","soya_bean","brown_salt","animal_salt","pig_concentrate","coconut","wonder_pig","big_pig"]

PRODUCT_CHOICES = (("broilers_marsh","broilers_marsh")
,("chick_marsh","chick_marsh")
,("growers_marsh","growers_marsh")
,("pig_marsh","pig_marsh")
,("layers_marsh","layers_marsh")
)



class ProductSalesForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	# date = models.DateField()
	product = forms.ChoiceField(choices = PRODUCT_CHOICES)
	quantity = forms.DecimalField(initial = 0)
	selling_price = forms.DecimalField(initial = 0)
	# total = forms.DecimalField(initial = 0)

	total = forms.DecimalField(
        widget=calculation.FormulaInput('quantity*selling_price') # <- using single math expression
    )
	
	class Meta:
		model = ProductSales

		fields = ["date","product","quantity","selling_price","total"]

class RawMaterialSalesForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())

	time = forms.TimeField(initial=timezone.now())
	raw_material = forms.ChoiceField(choices=RAW_MATERIAL_CHOICES)
	quantity = forms.DecimalField(initial = 0.0)
	selling_price = forms.DecimalField(initial = 0.0)
	total = forms.DecimalField(
        widget=calculation.FormulaInput('quantity*selling_price') # <- using single math expression
    )
	# total = forms.DecimalField(initial = 0)
	class Meta:
		model = RawMaterialSales
		fields = ["date","time","raw_material","quantity","selling_price","total"]