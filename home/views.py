from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'home.html')

def bill(request):
    return render(request,'invoice.html')
def client(request):
    return render(request,'client.html')

def addclient(request):
    return render(request,'addclient.html')

def itemreturn(request):
    return render(request,'itemreturn.html')

def stock(request):
    return render(request, 'stock.html')

def stock_edit(request):
    return render(request, 'edit-stock.html')
