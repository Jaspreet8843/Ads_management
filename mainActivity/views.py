from django.shortcuts import render, redirect
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