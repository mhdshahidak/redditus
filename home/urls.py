from . import views
from django.urls import path

app_name ='home'

urlpatterns = [

    path('', views.index, name="index"),

    # billing 
    path('billing', views.bill, name="billing"),
    path('clientsearch', views.client_search , name="clientsearch"),
    path('itemsearch', views.itemsearch, name='itemsearch'),
    path('clientadd', views.clientadd, name='clientadd'),
    
    path('billadding',views.bill_adding, name='billadding'),

    # client
    path('client', views.client,name='client'),
    path('addclient', views.addclient,name='addclient'),
    path('editclient', views.editclient,name='editclient'),

    # return
    path('itemreturn', views.itemreturnlist,name='itemreturn'),
    path('addeditemreturn/<str:id>', views.itemreturn, name='addeditemreturn'),

    # invoice 
    
    path('viewinvoice', views.viewInvoice, name='viewinvoice'),

    # stock
    path('stock', views.stock, name="stock"),
    path('stockedit/<int:id>', views.stock_edit, name="stockedit"),
    path('addstock', views.addstock, name="addstock"),
    path('deleteitem/<int:id>', views.deleteItem, name="deleteitem"),

    #expense
    path('expense', views.expense, name="expense"),
    path('addexpense', views.addexpense, name="addexpense"),
    path('editexpense/<int:id>', views.editexpense, name="editexpense"),

    # income
    path('income', views.income, name="income"),
    path('addincome', views.addincome, name="addincome"),
    path('editincome', views.editincome, name="editincome"),

    # payments
    path('payments', views.payments, name="payments"),
    path('addbank', views.bank, name="addbank"),

    # login
    path('login', views.login, name="login"),
  
]