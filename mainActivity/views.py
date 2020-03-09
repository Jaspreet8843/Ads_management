from django.shortcuts import render
from .models import customer,prices
# Create your views here.

def index(request):
    #c=customer.objects.filter(cust_type="govt")
    #p=prices(cust_type=c[0], price='10000')

    return render(request,'index.html')

def view_prices(request):
    p=prices.objects.all()
    return render(request,'view_prices.html',({'prices':p}))

def edit_prices(request):
    p=prices.objects.all()
    if request.method=='POST':
        if form.is_valid():
            pass

    return render(request,'edit_prices.html',({'prices':p}))