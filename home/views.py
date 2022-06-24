from django.shortcuts import redirect, render

from home.models import Billing, Catagory, Stock,Client

from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

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
    client = Client.objects.all()
    stock = Stock.objects.all()
    if Billing.objects.exists():
        bill = Billing.objects.last().id
        bill_id = 'RDTS'+str(1000+bill)
    else:
        bill=0
        bill_id = 'RDTS'+str(1000+bill)
    context = {
        "is_bill":True,
        'client':client,
        'stock':stock,
        'billid':bill_id,
    }
    return render(request,'invoice.html',context)


# client_search for billing

def client_search(request):
    phone = request.GET['phone']
    client_ex = Client.objects.filter(phone_no=phone).exists()
    if client_ex:
        client = Client.objects.get(phone_no=phone)
        data = {
            'name':client.client_name
        }
        return JsonResponse({'client':data})


# itemsearch

def itemsearch(request):
    item = request.GET['itemname']
    item_ex = Stock.objects.filter(item_name = item).exists()
    if item_ex:
        item_details = Stock.objects.get(item_name = item)
        data = {
            'item':item_details.item_catagory.cat_name,
            'rentalprice':item_details.rental_price
        }
        return JsonResponse(data)


# bill adding
# @csrf_exempt
# def data_adding(request):
#     cust_phone = request.POST['customer_phone']
#     inv_id = request.POST['invoiceId']
#     gst = request.POST['gst']
#     grand_total = request.POST['grand_total']
#     med_name = request.POST['medicinename']
#     qty = request.POST['qty']
#     payment_type = request.POST['type']
#     item_total = request.POST['itemtotal']
#     # print(gst)

#     cust_exists = Customers.objects.filter(phone=cust_phone).exists()
#     if cust_exists:
#         customer = Customers.objects.get(phone=cust_phone)
#         product = BranchProducts.objects.get(product__name=med_name,branch=request.session['branch'])
#         new_bill = Invoive(invoice_no=inv_id,customer=customer,product=product,quantity=qty,total=item_total,payment_methode=payment_type,gst=gst,grand_total=grand_total)
#         # print(new_bill)
#         new_bill.save()
#         product.quantity = product.quantity - int(qty)
#         product.save()
#         return JsonResponse({'msg':'BILL GENERATED'})
#     return JsonResponse({'msg':'BILL GENERATED'})


# client

def client(request):
    client_list = Client.objects.all()
    context = {
        "is_client":True,
        'client_list':client_list,
    }
    return render(request,'client.html',context)

def addclient(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']

        client_exist=Client.objects.filter(phone_no=phone).exists()
        if not client_exist:
            client = Client(client_name = name, phone_no = phone, address = address)
            client.save()
            context = {
            "is_addclient":True,
            "status":1,    
            }
            return render(request,'addclient.html',context)
        else:
            context = {
            "is_addclient":True,
            "status":2,    
            }
            return render(request,'addclient.html',context)
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
    stock = Stock.objects.all()
    context = {
        "is_stock":True,
        "stock":stock,
    }
    return render(request, 'stock.html',context)
    

def addstock(request):
    allcatagory = Catagory.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['catagories']
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
            "allcatagory":allcatagory,
            "status":1
            }
            return render(request, 'addstock.html',context)
        else:
            catagory = Catagory.objects.get(cat_name=category)
            addStock = Stock(item_name=name,item_catagory=catagory,quantity=qty,buying_price=price,rental_price=rentalPrice,damage_price=damagePrice,missing_price=missingPrice)
            addStock.save()
            context = {
            "is_stock":True,
            "allcatagory":allcatagory,
            "status":1
            }
            return render(request, 'addstock.html',context)
    context = {
        "is_stock":True,
        "allcatagory":allcatagory,
    }
    return render(request, 'addstock.html',context)

def stock_edit(request,id):
    item = Stock.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        qty = request.POST['qty']
        priceperday = request.POST['priceperday']
        damageprice = request.POST['damageprice']
        missprice = request.POST['missprice']

        Stock.objects.filter(id=id).update(item_name=name,quantity=qty,rental_price=priceperday,damage_price=damageprice,missing_price=missprice)
        return redirect('home:stock')

    context = {
        "is_stock_edit":True,
        "item":item,
    }
    return render(request, 'edit-stock.html',context)



def deleteItem(request,id):
    Stock.objects.get(id=id).delete()
    return redirect('/stock')

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