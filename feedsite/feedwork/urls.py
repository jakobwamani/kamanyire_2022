from django.urls import path

from feedwork import views

urlpatterns = [

    path('', views.index, name='index'),
    path('supply',views.supplying,name='get_supply'),
    path('view_supplies', views.viewing_supplies, name = 'view_supply'),
    path('update_supply/', views.updating_supplies, name = 'update_supply'),
    path('delete_supply/',views.deleting_supplies, name = 'delete_supply'),
    

]