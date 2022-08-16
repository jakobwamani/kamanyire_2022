from django.contrib import admin

from feedwork.models import *
# Register your models here.

admin.site.register(raw_materials)
admin.site.register(products)
admin.site.register(suppliers)
admin.site.register(logistics)
admin.site.register(purchases)
admin.site.register(raw_material_sales)
admin.site.register(raw_material_separations)
admin.site.register(product_names)
admin.site.register(product_sales)
admin.site.register(expenses)
admin.site.register(expense_names)
admin.site.register(expense_units)
admin.site.register(employee)
admin.site.register(employment_terms)
admin.site.register(advance_payments)
admin.site.register(salary_payments)