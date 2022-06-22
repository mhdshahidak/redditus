from django.shortcuts import render

from home.models import Catagory, Stock

# Create your views here.


def login(request):
    return render(request, 'login.html')


def index(request):
    context = {
        "is_index":True,
    }
    return render(request,'home.html',context)


# billing
def bill(request):
    context = {
        "is_bill":True,
    }
    return render(request,'invoice.html',context)


# client

def client(request):
    context = {
        "is_client":True,
    }
    return render(request,'client.html',context)

def addclient(request):
    context = {
        "is_addclient":True,
    }
    return render(request,'addclient.html',context)


def editclient(request):
    context = {
        "is_editclient":True,
    }
    return render(request,'editclient.html',context)


# return

def itemreturnlist(request):
    context = {
        "is_itemreturn":True,
    }
    return render(request,'itemreturn.html',context)


def itemreturn(request):
    context = {
        "is_itemreturn":True,
    }
    return render(request,'additemreturn.html',context)


# invoice
def viewInvoice(request):
    context = {
        "is_itemreturn":True,
    }
    return render(request,'viewinvoice.html',context)


# stock
def stock(request):
    context = {
        "is_stock":True,
    }
    return render(request, 'stock.html',context)
    

def addstock(request):
    catagory = Catagory.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['catagory']
        qty = request.POST['qty']
        missingPrice = request.POST['missing_price']
        rentalPrice = request.POST['rental_price']
        damagePrice = request.POST['damage_price']
        price = request.POST['price']

        category_exist=Catagory.objects.filter(cat_name=category).exists()
        if not category_exist:
            new_category=Catagory(cat_name=category)
            new_category.save()
            addStock = Stock(item_name=name,item_catagory=new_category,quantity=qty,buying_price=price,rental_price=rentalPrice,damage_price=damagePrice,missing_price=missingPrice)
            addStock.save()
            context = {
            "is_stock":True,
            "catagory":catagory,
            "status":1
            }
            return render(request, 'addstock.html',context)
        else:
            catagory = Catagory.objects.get(cat_name=category)
            addStock = Stock(item_name=name,item_catagory=catagory,quantity=qty,buying_price=price,rental_price=rentalPrice,damage_price=damagePrice,missing_price=missingPrice)
            addStock.save()
            context = {
            "is_stock":True,
            "catagory":catagory,
            "status":1
            }
            return render(request, 'addstock.html',context)

    context = {
        "is_stock":True,
        "catagory":catagory,
    }
    return render(request, 'addstock.html',context)

def stock_edit(request):
    context = {
        "is_stock_edit":True,
    }
    return render(request, 'edit-stock.html',context)

# expence

def expense(request):
    context = {
        "is_expense":True,

    }
    return render(request, 'expense.html', context)


def addexpense(request):
    context = {
        "is_expense":True,

    }
    return render(request, 'addexpense.html', context)


def editexpense(request):
    context = {
        "is_expense":True,

    }
    return render(request, 'editexpense.html', context)


# income
def income(request):
    context = {
        "is_income":True,

    }
    return render(request, 'income.html', context)


def addincome(request):
    context = {
        "is_income":True,

    }
    return render(request, 'addincome.html', context)


def editincome(request):
    context = {
        "is_income":True,

    }
    return render(request, 'editincome.html', context)


# payments

def payments(request):
    context = {
        "is_payments":True,
    }
    return render(request, 'payments.html', context)


def bank(request):
    context = {
        "is_payments":True,
    }
    return render(request, 'addbank.html', context)