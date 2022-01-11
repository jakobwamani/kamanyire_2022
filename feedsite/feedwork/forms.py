from django import forms
from feedwork.models import *
from django.utils import timezone

RAW_MATERIAL_CHOICES = (("maize_bran" , "maize_bran"),("cotton", "cotton")
,("sun_flower" , "sun_flower")
,("fish" , "fish")
,("salt" ,"salt")
,("calcium" , "calcium")
,("soya_bean","soya_bean")
,("animal_salt","animal_salt")
,("common_salt","common_salt")
,("coconut","coconut")
,("pig_concentrate","pig_concentrate")
,("wonder_pig","wonder_pig")
,("big_pig","big_pig")
,("general_purpose_premix" , "general_purpose_premix")
,("layers_premix" , "layers_premix")
,("shells" , "shells")
,("meat_boaster" , "meat_boaster")
,("egg_boaster" ,"egg_boaster"))
# creating a form
class RawMaterialForm(forms.ModelForm):

  	
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
    #birth_date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
	receipt_number = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	supplier = forms.CharField()
	item = forms.ChoiceField(choices=RAW_MATERIAL_CHOICES)
	# item = forms.CharField()
	quantity = forms.IntegerField(disabled=True)
	increase_quantity = forms.IntegerField(initial=0)
	reduce_quantity = forms.IntegerField(initial=0)
	unit_price = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	# i  cannot edit this stuff from right here so all amounts will shown in the retrieve view
	# amount = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	transport = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	onloading = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	offloading = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	grinding = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	# i  cannot edit this stuff from right here so all amounts will shown in the retrieve view
	# fullamount = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	# pricing = forms.IntegerField(help_text='First check to cost of supply to update this')
   
	# create meta class
	class Meta:
		# specify model to be used
		model = RawMaterial

		# exclude = ["amount","fullamount",]
		fields = [
			
			"date",
			"receipt_number",
			"supplier",
			"item","quantity","increase_quantity","reduce_quantity","unit_price", "transport","onloading","offloading","grinding",
		]

#supply form
class SupplyForm(forms.ModelForm):

  	
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
    #birth_date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))
	receipt_number = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	supplier = forms.CharField()
	item = forms.ChoiceField(choices=RAW_MATERIAL_CHOICES)
	# item = forms.CharField()
	quantity = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	unit_price = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	# i  cannot edit this stuff from right here so all amounts will shown in the retrieve view
	# amount = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	transport = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	onloading = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	offloading = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	grinding = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	# i  cannot edit this stuff from right here so all amounts will shown in the retrieve view
	# fullamount = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	# pricing = forms.IntegerField(help_text='First check to cost of supply to update this')
   
	# create meta class
	class Meta:
		# specify model to be used
		model = RawMaterial

		# exclude = ["amount","fullamount",]
		fields = [
			"date",
			"receipt_number",
			"supplier",
			"item","quantity","unit_price", "transport","onloading","offloading","grinding",
		]


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
,("old_pig","old_pig")
,("layers_marsh","layers_marsh")
,("young_pig","young_pig"))
class ProductForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	# date = forms.DateField()
	product = forms.ChoiceField(choices=PRODUCT_CHOICES)
	fish = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	maize_bran = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	cotton = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	sun_flower = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	salt = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	layers_premix = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	general_purpose_premix = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	shells = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	meat_boaster = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	egg_boaster = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	#added items
	calcium = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	soya_bean = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	animal_salt = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	common_salt = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	brown_salt = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	coconut = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	pig_concentrate = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	wonder_pig = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	big_pig = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)

	class Meta:
		model = Product

		fields = ["date","product","maize_bran","cotton","sun_flower","salt","layers_premix","general_purpose_premix","shells","meat_boaster","egg_boaster","fish","calcium","soya_bean","animal_salt","common_salt","brown_salt","coconut","pig_concentrate","wonder_pig","big_pig"]


class ProductPriceForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	broilers_marsh = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	chick_marsh = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	old_pig = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	growers_marsh = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	layers_marsh = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	young_pig = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)

	class Meta:
		model = ProductPrices

		fields = ["date","broilers_marsh","chick_marsh","old_pig","growers_marsh","layers_marsh","young_pig"]



class RawMaterialPricesForm(forms.ModelForm):
	# quantity_id = models.AutoField(primary_key=True)
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	# date = models.DateField()
	maize_bran = forms.IntegerField(initial=0)
	cotton = forms.IntegerField(initial=0)
	sun_flower = forms.IntegerField(initial=0)
	fish = forms.IntegerField(initial=0)
	salt = forms.IntegerField(initial=0)
	general_purpose_premix = forms.IntegerField(initial=0)
	layers_premix = forms.IntegerField(initial=0)
	shells = forms.IntegerField(initial=0)
	meat_boaster = forms.IntegerField(initial=0)
	egg_boaster = forms.IntegerField(initial=0)

	class Meta:
		model = RawMaterialPrices

		fields = ["date","maize_bran","cotton","sun_flower","salt","layers_premix","general_purpose_premix","shells","meat_boaster","egg_boaster","fish"]


PRODUCT_CHOICES = (("broilers_marsh","broilers_marsh")
,("chick_marsh","chick_marsh")
,("growers_marsh","growers_marsh")
,("old_pig","old_pig")
,("layers_marsh","layers_marsh")
,("young_pig","young_pig"))
class ProductSalesForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	# date = models.DateField()
	product = forms.ChoiceField(choices = PRODUCT_CHOICES)
	quantity = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	selling_price = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	total = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)

	class Meta:
		model = ProductSales

		fields = ["date","product","quantity","selling_price","total"]

class RawMaterialSalesForm(forms.ModelForm):
	YEARS= [x for x in range(2000,2030)]
	date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=YEARS),initial=timezone.now())
	raw_material = forms.ChoiceField(choices=RAW_MATERIAL_CHOICES)
	quantity = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	selling_price = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)
	total = forms.DecimalField(max_digits=10, decimal_places=2 , initial=0.0)

	class Meta:
		model = RawMaterialSales

		fields = ["date","raw_material","quantity","selling_price","total"]