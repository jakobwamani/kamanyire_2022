from django.urls import path
from django.conf.urls import include
from feedwork import views
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [

    path('', views.index, name='index'),
    # path('',views.creating_net_income,name = "index"),
    path('supply',views.creating_supplies,name='get_supply'),
    path('view_supplies', views.viewing_supplies, name = 'view_supply'),
    path('update_supply/', views.updating_supplies, name = 'update_supply'),
    path('delete_supply/',views.deleting_supplies, name = 'delete_supply'),
    path('product',views.create_product, name = 'create_product'),
    path('view_products',views.viewing_product, name = 'view_product'),
    path('update_products/',views.updating_product, name = 'update_product'),
    path('delete_products/',views.deleting_product, name = 'delete_product'),
    path('create_raw_material_prices/',views.create_raw_material_prices, name = 'raw_material_prices'),
    path('view_raw_material_prices/',views.viewing_raw_material_prices, name = 'view_raw_material_prices'),
    path('update_raw_material_prices/',views.updating_raw_material_prices, name = 'update_raw_material_prices'),
    path('delete_raw_material_prices/',views.deleting_raw_material_prices, name = 'delete_raw_material_prices'),
    path('create_product_prices/',views.creating_product_prices, name = 'create_product_prices'),
    path('view_product_prices/',views.viewing_product_prices, name = 'view_product_prices'),
    path('update_product_prices/',views.updating_product_prices, name= 'update_product_prices'),
    path('delete_product_prices/',views.deleting_product_prices, name = 'delete_product_prices'),
    path('do_product_sales/',views.doing_product_sales, name = 'product_sales'),
    path('view_product_sales/',views.viewing_product_sales, name = 'view_product_sales'),
    path('update_product_sales/',views.updating_product_sales, name = 'update_product_sales'),
    path('delete_product_sales/',views.deleting_product_sales,name = 'delete_product_sales'),
    path('do_raw_material_sales/',views.doing_raw_material_sales, name = 'raw_material_sales'),
    path('view_raw_material_sales/',views.viewing_raw_material_sales, name = 'view_raw_material_sales'),
    path('update_raw_material_sales/',views.updating_raw_material_sales, name='update_raw_material_sales'),
    path('delete_raw_material_sales/',views.deleting_raw_material_sales, name ='delete_raw_material_sales'),
    path('expense/',views.getting_expenses, name='expenses'),
    path('view_expenses/',views.viewing_expenses, name='view_expenses'),
    path('update_expenses/',views.updating_expenses, name='update_expenses'),
    path('delete_expenses/',views.deleting_expenses, name='delete_expenses'),
    url(r'^report_builder/', include('report_builder.urls')),
    # path('api-auth/', include('rest_framework.urls'))
    ]