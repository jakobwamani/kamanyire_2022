from django.urls import path

from feedwork import views

urlpatterns = [

    path('', views.index, name='index'),
    path('supply',views.supplying,name='get_supply'),
    path('view_supplies', views.viewing_supplies, name = 'view_supply'),
    path('update_supply/', views.updating_supplies, name = 'update_supply'),
    path('delete_supply/',views.deleting_supplies, name = 'delete_supply'),
    path('product',views.create_product, name = 'create_product'),
    path('view_products',views.viewing_product, name = 'view_product'),
    path('update_products/',views.updating_product, name = 'update_product'),
    path('delete_products/',views.deleting_product, name = 'delete_product'),
    

]