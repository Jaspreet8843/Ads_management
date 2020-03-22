import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import customer,prices,adverts
import time
# Create your views here.

def index(request):
    #c=customer.objects.filter(cust_type="govt")
    #p=prices(cust_type=c[0], price='10000')

    return render(request,'index.html')

#PRICES--------------------------------------------------------------------------------
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
        else:
            print("Entries can't be empty")
        return redirect('view_prices')

    return render(request,'edit_prices.html',({'prices':p}))

def delete(request, no):
    p=prices.objects.filter(id=no).delete()
    return redirect(edit_prices)

#CUSTOMER-------------------------------------------------------------------------------
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
        else:
            print("Entries can't be empty")
        return redirect('index')
    return render(request,'add_customer.html')

def view_customers(request):
    cust = customer.objects.all()
    return render(request,'view_customers.html',({'customers':cust}))


#ADVERTISEMENTS----------------------------------------------------------------------------
def add_advert(request):
    if request.method=='POST':
        cust_name=request.POST.get('customer_name')
        cust_id=request.POST.get('customer_id')
        dis_from = request.POST.get('disp_from')
        dis_till = request.POST.get('disp_till')
        ad_header=request.POST.get('ad_header')
        ad_height=request.POST.get('ad_height')
        ad_width=request.POST.get('ad_width')
        ad_page=request.POST.get('ad_page')
        if(cust_name != '' and cust_id != '' and ad_header != '' and ad_height != '' 
            and ad_width != ''):
            customer_name=customer.objects.filter(cust_id=cust_id)
            obj=adverts(cust_name=customer_name[0].cust_name,cust_id=cust_id,ad_date_from=dis_from,ad_date_till=dis_till,ad_header=ad_header,ad_height=ad_height,
                ad_width=ad_width,ad_page=ad_page)
            obj.save()
        else:
            print("Entries can't be empty")
        return redirect('index')
    cust={}
    cust_obj=customer.objects.all()
    cust_name=[]
    cust_id=[]
    for c in cust_obj:
        cust_name.append(c.cust_name)
        cust_id.append(c.cust_id)
    cust['name']=cust_name
    cust['id']=cust_id
    return render(request,'add_advert.html',(cust))

def view_adverts(request):
    ads = adverts.objects.all()
    return render(request,'view_adverts.html',({'advertisements':ads}))

def billing(request):
    cust=customer.objects.all()
    if request.method=='POST':
        cust_id=request.POST.get('customer_id')
        ads=adverts.objects.filter(cust_id=cust_id)
        return render(request, 'billing.html', ({'cust':cust,'ads':ads}))
    return render(request, 'billing.html', ({'cust':cust}))

def view_schedule(request):
    schedule=[]
    if request.method=="POST":
        date_from=request.POST.get('from')
        date_upto=request.POST.get('upto')
        if date_from!='' or date_upto!='':
            schedule=adverts.objects.filter(ad_date_from__gte=date_from , ad_date_from__lte=date_upto).order_by('-ad_date_from')
        else:
            schedule=adverts.objects.all().order_by('ad_date_from')
    return render(request, 'view_schedule.html', ({'schedule':schedule}))