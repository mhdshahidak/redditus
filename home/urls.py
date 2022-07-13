from . import views
from django.urls import path

app_name ='home'

urlpatterns = [

    path('', views.index, name="index"),

    # billing 
    path('billing', views.bill, name="billing"),
    path('viewbill/<int:id>', views.view_bill, name="viewbill"),


    # add new product in bill
    path('addinbilling/<int:id>', views.addinbilling, name="addinbilling"),
    
    # add new product in bill Ajax
    path('newbilladding',views.new_bill_adding, name='newbilladding'),

    # bill ajax
    path('clientsearch', views.client_search , name="clientsearch"),
    path('itemsearch', views.itemsearch, name='itemsearch'),
    path('clientadd', views.clientadd, name='clientadd'),
    path('billadding',views.bill_adding, name='billadding'),

    # client
    path('client', views.client,name='client'),
    path('addclient', views.addclient,name='addclient'),
    path('editclient/<str:id>', views.editclient,name='editclient'),

    # return
    path('itemreturn', views.itemreturnlist,name='itemreturn'),
    path('addeditemreturn/<str:id>', views.itemreturn, name='addeditemreturn'),

    # return ajax
    path('returningitems', views.returningEachItems, name='returningitems'),

    # invoice 
    
    path('viewinvoice/<str:id>', views.viewInvoice, name='viewinvoice'),

    # payment ajax
    path('paynow', views.paymentMethod, name='paynow'),

    # stock
    path('stock', views.stock, name="stock"),
    path('stockedit/<int:id>', views.stock_edit, name="stockedit"),
    path('addstock', views.addstock, name="addstock"),
    path('deleteitem/<int:id>', views.deleteItem, name="deleteitem"),

    #expense
    path('expense', views.expense, name="expense"),
    path('addexpense', views.addexpense, name="addexpense"),
    path('editexpense/<int:id>', views.editexpense, name="editexpense"),
    path('deleteexpense/<int:id>',views.deleteExpense,name='deleteexpense'),

    # income
    path('income', views.income, name="income"),
    path('addincome', views.addincome, name="addincome"),
    path('editincome/<int:id>', views.editincome, name="editincome"),
    path('deleteincome/<int:id>', views.deleteIncome,name='deleteincome'),

    # payments
    path('payments', views.payments, name="payments"),
    path('addbank', views.bank, name="addbank"),

    #payment ajax
    path('deletebank/<int:id>', views.deletebank, name="deletebank"),

    # login
    path('loginpage', views.loginpage, name="loginpage"),
    path('logout_view', views.logout_view,name="logout_view"),
  
]