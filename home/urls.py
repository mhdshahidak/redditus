from . import views
from django.urls import path

app_name ='home'

urlpatterns = [

    path('', views.index, name="index"),
    path('billing', views.bill, name="billing"),
    path('client',views.client,name='client'),
    path('addclient',views.addclient,name='addclient'),
    path('itemreturn',views.itemreturn,name='itemreturn'),
    path('index',views.index,name='index'),
    path('stock', views.stock, name="stock"),
    path('stock_edit', views.stock_edit, name="stock_edit"),

  
]