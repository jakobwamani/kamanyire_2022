from django.urls import path

from feedwork import views

urlpatterns = [

    path('index', views.index, name='index'),
    path('supply',views.supplying,name='get_supplies'),
    path('view_supplies', views.viewing_supplies, name = 'view_supplies'),
    

]