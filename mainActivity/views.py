from django.shortcuts import render, redirect
from .models import customer,prices
import time
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
        new_cust=request.POST.get('cus_type')
        new_price=request.POST.get('cus_price')
        for price in p:
            pr=prices.objects.get(id=price.id)
            pr.price=request.POST.get(str(price.id))
            pr.save()
        if(new_cust != '' and new_price != ''):
            obj=prices(cust_type=new_cust, price=new_price)
            obj.save()
        return redirect('view_prices')

    return render(request,'edit_prices.html',({'prices':p}))

def delete(request, no):
    p=prices.objects.filter(id=no).delete()
    return redirect(edit_prices)

def add_customer(request):
    if request.method=='POST':
        cust_name=request.POST.get('customer_name')
        cust_address=request.POST.get('customer_address')
        cust_phone=request.POST.get('customer_phone')
        cust_type=request.POST.get('customer_type')
        cust_id=request.POST.get('customer_id')
        cust_since=time.strftime('%Y-%m-%d')
        if(cust_name != '' and cust_address != '' and cust_phone != '' and cust_type != '' 
            and cust_id != ''):
            obj=customer(cust_name=cust_name,cust_address=cust_address,cust_phone=cust_phone,
                  cust_type=cust_type,cust_id=cust_id,cust_since=cust_since)
            obj.save()
        return redirect('index')
    return render(request,'add_customer.html')

def view_customers(request):
    c=customer.objects.all()
    return render(request,'view_customers.html',({'customers':c}))