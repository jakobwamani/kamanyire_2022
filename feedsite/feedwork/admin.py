from django.contrib import admin

from feedwork.models import *
# Register your models here.

admin.site.register(RawMaterial)
admin.site.register(Product)
admin.site.register(RawMaterialQuantities)
admin.site.register(ProductQuantities)
admin.site.register(ProductPrices)
admin.site.register(RawMaterialPrices)
admin.site.register(ProductSales)
admin.site.register(RawMaterialSales)
admin.site.register(Expenses)
admin.site.register(RawMaterialProfits)
admin.site.register(ProductProfits)