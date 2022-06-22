from . import views
from django.urls import path

app_name ='home'

urlpatterns = [

    path('', views.index, name="index"),

    # billing 
    path('billing', views.bill, name="billing"),

    # client
    path('client', views.client,name='client'),
    path('addclient', views.addclient,name='addclient'),
    path('editclient', views.addclient,name='editclient'),

    # return
    path('itemreturn', views.itemreturnlist,name='itemreturn'),
    path('additemreturn', views.itemreturn, name='additemreturn'),

    # invoice 
    
    path('viewinvoice', views.viewInvoice, name='viewinvoice'),

    # stock
    path('stock', views.stock, name="stock"),
    path('stock_edit', views.stock_edit, name="stock_edit"),
    path('addstock', views.addstock, name="addstock"),

    #expense
    path('expense', views.expense, name="expense"),
    path('addexpense', views.addexpense, name="addexpense"),
    path('editexpense', views.editexpense, name="editexpense"),

    # income
    path('income', views.income, name="income"),
    path('addincome', views.addincome, name="addincome"),
    path('editincome', views.editincome, name="editincome"),

    # payments
    path('payments', views.payments, name="payments"),
    path('addbank', views.bank, name="addbank"),

    # login
    path('login', views.login, name="login")
  
]