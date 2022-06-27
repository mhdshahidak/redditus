from ast import Return
from datetime import datetime
from django.shortcuts import redirect, render

from home.models import Bank, Billing, BillingProducts, Catagory, Stock,Client, expence, expencecatagory

from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.db.models import Count


# Create your views here.


def login(request):
    return render(request, 'login.html')


def index(request):
    bills = Billing.objects.all().select_related('billingproducts__set').annotate(itemCount=Count('billingproducts')).values('id','itemCount','billing_no','billing_date','client__client_name')
    context = {
        "is_index":True,
        'bills':bills,
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
    # else:
    #     new_client = Client(phone_no=phone)
    #     new_client.save()
    #     data = {
    #         'name':"",
    #     }
    #     return JsonResponse({'client':data})

# itemsearch

def itemsearch(request):
    item = request.GET['itemname']
    item_ex = Stock.objects.filter(item_name = item).exists()
    if item_ex:
        item_details = Stock.objects.get(item_name = item)
        data = {
            'item':item_details.item_catagory.cat_name,
            'rentalprice':item_details.rental_price,
            'max_qty':item_details.quantity
        }
        return JsonResponse(data)

# add client in bill
@csrf_exempt
def clientadd(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        invId = request.POST['invId']
        date= datetime.now()
        phone_ex= Client.objects.filter(phone_no = phone).exists()
        if not phone_ex:
            client_obj = Client(client_name=name, phone_no=phone)
            client_obj.save()
            inv_obj = Billing(billing_no=invId, client=client_obj, billing_date=date)
            inv_obj.save()
            data ={
                'invId':invId,
                'invpk':inv_obj.id
            }
            return JsonResponse(data)
        else:
            client =  Client.objects.get(phone_no = phone)
            inv_obj = Billing(billing_no=invId, client=client, billing_date=date)
            inv_obj.save()
            data = {
                'invId':invId,
                'invpk':inv_obj.id
            }
            return JsonResponse(data)

            


# bill adding
@csrf_exempt
def bill_adding(request):
    invid = request.POST['invid']
    # customer_phone = request.POST['customer_phone']
    item = request.POST['item']
    qty = request.POST['qty']
 
    # print(gst)
    inv_obj = Billing.objects.get(id=invid)
      
    item = Stock.objects.get(item_name=item)
    date = datetime.now()
    new_item = BillingProducts(billing=inv_obj,item=item,qty=qty,billing_date=date)
    new_item.save()
    item.quantity = item.quantity - int(qty)
    item.save()
    
    return JsonResponse({'msg':'BILL GENERATED'})
   


# client

def client(request):
    bills = Billing.objects.all().select_related('billingproducts__set').annotate(itemCount=Count('billingproducts')).values('id','itemCount','billing_no','billing_date','client__client_name','client__phone_no')
    
    # print(5*"*")
    client_list = Client.objects.all()
    context = {
        "is_client":True,
        'client_list':client_list,
        "bills":bills,
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


def editclient(request, id):
    # print(id)
    client = Client.objects.get(phone_no=id)
    if request.method == 'POST':
        cid = request.POST['cid']
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        Client.objects.filter(id=cid).update(client_name=name,phone_no=phone,address=address)
        return redirect('home:client')
    context = {
        "is_editclient":True,
        "client":client,
    }
    return render(request,'editclient.html',context)


# return

def itemreturnlist(request):

    bills = Billing.objects.all().select_related('billingproducts__set').annotate(itemCount=Count('billingproducts')).values('id','itemCount','billing_no','billing_date','client__client_name','client__phone_no')
    
    context = {
        "is_itemreturn":True,
        'return':bills,
    }
    return render(request,'itemreturn.html',context)


def itemreturn(request, id):
    bill = Billing.objects.get(id=id)
    items= BillingProducts.objects.filter(billing = bill)
    context = {
        "is_itemreturn":True,
        'items':items,
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
    expences = expence.objects.all()
    context = {
        "is_expense":True,
        "expences":expences,

    }
    return render(request, 'expense.html', context)


def addexpense(request):
    catagory = expencecatagory.objects.all()
    if request.method == 'POST':
        catagory = request.POST['catag']
        note = request.POST['note']
        date = request.POST['date']
        amount = request.POST['amount']

        catagory_exists = expencecatagory.objects.filter(catagory=catagory).exists()

        if catagory_exists:
            catagorys = expencecatagory.objects.get(catagory=catagory)
            new_expence = expence(date=date,catagory=catagorys,note=note,amount=amount)
            new_expence.save()
            context = {
                "is_expense":True,
                "catagory":catagory,
                "status":1,
            }
            return render(request, 'addexpense.html', context)

        else:
            new_catagory = expencecatagory(catagory=catagory)
            new_catagory.save()
            new_expence = expence(date=date,catagory=new_catagory,note=note,amount=amount)
            new_expence.save()
            context = {
                "is_expense":True,
                "catagory":catagory,
                "status":1,
            }
            return render(request, 'addexpense.html', context)
    context = {
        "is_expense":True,
        "catagory":catagory,

    }
    return render(request, 'addexpense.html', context)


def editexpense(request, id):
    expences = expence.objects.get(id=id)
    category = expencecatagory.objects.all()
    if request.method == 'POST':
        category_in = request.POST['category']
        date = request.POST['date']
        note = request.POST['note']
        amount= request.POST['amount']

        category_ex = expencecatagory.objects.filter(catagory=category_in).exists()
        if not category_ex:
            cat = expencecatagory(catagory=category_in)
            cat.save()
            cat_in =expencecatagory.objects.get(catagory=category_in)
            expense_obj=expence.objects.filter(id=id).update(date=date, catagory=cat_in, note=note, amount=amount)
        else:
            cat_in =expencecatagory.objects.get(catagory=category_in)
            expense_obj=expence.objects.filter(id=id).update(date=date, catagory=cat_in, note=note, amount=amount)
        return redirect('home:expense')
    context = {
        "is_expense":True,
        'category':category,
        'expence':expences,

    }
    return render(request, 'editexpense.html', context)


def deleteExpense(request, id):
    delete_expence = expence.objects.filter(id=id).delete()
    return redirect('home:expense')

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
    if request.method == 'POST':
        bank_name = request.POST['bank_name']
        ifsc= request.POST['ifsc']
        acc_no = request.POST['acc_no']
        conf_acc_no = request.POST['conf_acc_no']
        acc_holder_name = request.POST['acc_holder_name']
        branch = request.POST['branch']
        district = request.POST['district']
        address = request.POST['address']
        if conf_acc_no == acc_no:
            bank_ex = Bank.objects.filter(bank_name=bank_name, acc_number=acc_no).exists()
            if not bank_ex:
                add_bank = Bank(bank_name=bank_name, acc_holder_name=acc_holder_name, ifsc_code=ifsc, acc_number=acc_no, branch=branch, district=district, address=address)
                add_bank.save()
                return render(request, 'addbank.html',{'status':1})
            else:
                return render(request, 'addbank.html',{'success':3})
        else:
            return render(request, 'addbank.html',{'status':2})
    context = {
        "is_payments":True,
    }
    return render(request, 'addbank.html', context)