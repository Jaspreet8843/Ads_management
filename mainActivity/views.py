from django.db.models import Q
import datetime
from django.shortcuts import render, redirect
from .models import customer, prices, adverts, rejected, bills, payments, users
from django.utils import timezone
from django.forms.models import  model_to_dict
import time
from copy import copy

# FOR REPLACEMENT OF RAW QUERIES
def join_tables(t1, t2):
    list1=t1
    list2=t2
    list3=[]
    for item1 in list1:
        for item2 in list2:
            it = copy(item1)
            for item, val in item2.items():
                if item not in item1:
                    it[item] = val
                else:
                    it[item + "_COPY"] = val
            list3.append(it)
    return list3

# FOR CONNECTING TWO TABLES
def conn(table, col1, col2):
    new_table=[]
    for row in table:
        if row[col1]==row[col2]:
            new_table.append(row)
    return new_table


# Create your views here.

def index(request):
    # c=customer.objects.filter(cust_type="govt")
    # p=prices(cust_type=c[0], price='10000')
    if request.session.has_key('username'):
        date_today=datetime.date.today()
        today = adverts.objects.filter(ad_date_from__lte=date_today, ad_date_till__gte=date_today, ad_status='approved')
        return render(request, 'localsdirectory/index.html',({'tab':"home",'today':today,'date':date_today}))
    else:
        return redirect('login')

def login(request):
    if request.method=='POST':
        user_id=request.POST.get('login_id')
        user_pass=request.POST.get('login_pass')
        if user_id=="admin" and user_pass=="admin":
            request.session['username'] = "admin"
            print("User logged in!")
            return redirect('index')
        else:
            user = users.objects.filter(user_id=user_id,user_pass=user_pass)
            if user.exists():
                request.session['username']=user_id
                return redirect('index')
    return render(request,'login.html')

def logout(request):
    del request.session['username']
    return redirect('login')

def adduser(request):
    if request.session.has_key('username') and request.session['username']=="admin":
        if request.method=='POST':
            user_name=request.POST.get('name')
            user_id=request.POST.get('user_id')
            user_pass=request.POST.get('user_pass')
            if(user_name!='' and user_id!='' and len(user_pass)>=8):
                obj = users(user_name=user_name,user_id=user_id,user_pass=user_pass)
                obj.save()
                print("User added successfully")
            else:
                print("Invalid entries")
                return redirect('adduser')
            return redirect('index')
        allusers = users.objects.all()
        return render(request,'add_user.html',({'users':allusers}))
    else:
        return redirect('index')


# PRICES--------------------------------------------------------------------------------
def view_prices(request):
    if request.session.has_key('username'):
        p = prices.objects.all()
        return render(request, 'view_prices.html', ({'prices': p}))
    else:
        return redirect('login')


def edit_prices(request):
    if request.session.has_key('username'):
        p = prices.objects.all()
        if request.method == 'POST':
            new_cust = request.POST.get('cus_type')
            new_price = request.POST.get('cus_price')
            for price in p:
                pr = prices.objects.get(id=price.id)
                pr.price = request.POST.get(str(price.id))
                pr.save()
            if (new_cust != '' and new_price != ''):
                obj = prices(cust_type=new_cust, price=new_price)
                obj.save()
            else:
                print("Entries can't be empty")
            return redirect('view_prices')

        return render(request, 'edit_prices.html', ({'prices': p}))
    else:
        return redirect('login')


def delete(request, no):
    if request.session.has_key('username'):
        p = prices.objects.filter(id=no).delete()
        return redirect(edit_prices)
    else:
        return redirect('login')


# CUSTOMER-------------------------------------------------------------------------------
def add_customer(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            cust_name = request.POST.get('customer_name')
            cust_address = request.POST.get('customer_address')
            cust_phone = request.POST.get('customer_phone')
            cust_type = request.POST.get('customer_type')
            cust_id = request.POST.get('customer_id')
            cust_since = time.strftime('%Y-%m-%d')
            if (cust_name != '' and cust_address != '' and cust_phone != '' and cust_type != ''
                    and cust_id != ''):
                obj = customer(cust_name=cust_name, cust_address=cust_address, cust_phone=cust_phone,
                               cust_type=cust_type, cust_id=cust_id, cust_since=cust_since)
                obj.save()
            else:
                print("Entries can't be empty")
            return redirect('index')
        return render(request, 'add_customer.html',({'tab':"customers"}))
    else:
        return redirect('login')


def view_customers(request):
    if request.session.has_key('username'):
        cust = customer.objects.all()
        return render(request, 'view_customers.html', ({'customers': cust,'tab':"customers"}))
    else:
        return redirect('login')


# ADVERTISEMENTS----------------------------------------------------------------------------
def add_advert(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            cust_id = request.POST.get('customer_name')
            dis_from = request.POST.get('disp_from')
            dis_till = request.POST.get('disp_till')
            ad_header = request.POST.get('ad_header')
            ad_height = request.POST.get('ad_height')
            ad_width = request.POST.get('ad_width')
            ad_page = request.POST.get('ad_page')
            cust_name = customer.objects.filter(cust_id=cust_id)
            if (cust_name != '' and cust_id != '' and ad_header != '' and ad_height != ''
                    and ad_width != ''):
                customer_name = customer.objects.filter(cust_id=cust_id)
                obj = adverts(cust_name=customer_name[0].cust_name, cust_id=cust_id, ad_date_from=dis_from,
                              ad_date_till=dis_till, ad_header=ad_header, ad_height=ad_height,
                              ad_width=ad_width, ad_page=ad_page)
                obj.save()
            else:
                print("Entries can't be empty")
            return redirect('index')
        cust = customer.objects.filter()
        return render(request, 'add_advert.html', ({'cust':cust,'tab':"adv"}))
    else:
        return redirect('login')


def view_adverts(request):
    if request.session.has_key('username'):
        ads = adverts.objects.all()
        return render(request, 'view_adverts.html', ({'advertisements': ads,'tab':"adv"}))
    else:
        return redirect('login')



#BILLING---------------------------------------------------------------------------------
def billing(request):
    if request.session.has_key('username'):
        cust = customer.objects.filter()
        if request.method == 'POST':
            cust_id = request.POST.get('customer_id')
            ads = adverts.objects.filter(cust_id=cust_id, ad_status="Approved").order_by('ad_date_from')
            ads = ads.exclude(id__in=bills.objects.filter(cust_id=cust_id).values('ad_id'))
            print(ads.query)
            return render(request, 'billing.html', ({'cust': cust, 'ads': ads, 'customer_id': cust_id,'tab':"bills"}))
        return render(request, 'billing.html', ({'cust': cust,'tab':"bills"}))
    else:
        return redirect('login')


def view_bills(request):
    if request.session.has_key('username'):
        cust = customer.objects.filter()
        if request.method == 'POST':
            cust_id = request.POST.get('customer_id')
            # bill = adverts.objects.raw("""Select * from mainactivity_adverts ad, mainactivity_bills bill 
            # where bill.ad_id=ad.id and ad.cust_id=%s""", [cust_id])
            # bill = adverts.objects.raw("""Select * from mainactivity_adverts ad, mainactivity_bills bill where bill.ad_id=ad.id
            #  and ad.cust_id=%s""", [cust_id])
            # print(model_to_dict(cust[0]))
            bi=bills.objects.values('ad_id','price','gst','total')
            ad=adverts.objects.values('id','ad_header','ad_date_from','ad_date_till','ad_page').filter(cust_id=cust_id)
            joined=join_tables(bi,ad)
            connected=conn(joined,"ad_id","id")
            return render(request, 'view_bills.html', ({'bill': connected, 'cust': cust,'tab':"bills"}))
        return render(request, 'view_bills.html', ({'cust': cust,'tab':"bills"}))
    else:
        return redirect('login')


def store_bills(request, cust_id):
    if request.session.has_key('username'):
        if request.method == 'POST':
            ads = adverts.objects.filter(cust_id=cust_id, ad_status="Approved")
            ads = ads.exclude(id__in=bills.objects.filter(cust_id=cust_id).values('ad_id'))
            totals = []
            for i in range(ads.count()):
                if request.POST.get(str(ads[i].id)) != '':
                    totals.append(ads[i].id)
                    totals.append(request.POST.get(str(ads[i].id)))
            bill_date = time.strftime('%Y-%m-%d')
            for i in range(0, len(totals), 2):
                bill_total = float(totals[i + 1])
                bill_price = round(bill_total / 1.18, 2)
                bill_gst = round(bill_total - bill_price, 2)
                obj = bills(cust_id=cust_id, ad_id=totals[i], price=bill_price, gst=bill_gst, total=bill_total,
                            billing_date=bill_date)
                obj.save()
            return redirect('index')
        return render(request, 'index.html')
    else:
        return redirect('login')


def view_schedule(request):
    if request.session.has_key('username'):
        schedule = ''
        if request.method == "POST":
            date_from = request.POST.get('from')
            date_upto = request.POST.get('upto')
            if date_from != '' or date_upto != '':
                schedule = adverts.objects.filter(ad_date_from__gte=date_from, ad_date_from__lte=date_upto, ad_status='approved').order_by(
                    'ad_date_from')
            else:
                schedule = adverts.objects.filter(ad_status='approved').order_by('ad_date_from')
        return render(request, 'view_schedule.html', ({'schedule': schedule,'tab':"schedule"}))
    else:
        return redirect('login')


def pending_for_approval(request):
    if request.session.has_key('username'):
        schedule = adverts.objects.filter(ad_status='Pending for approval').order_by('ad_date_from')
        return render(request, 'pending_for_approval.html', ({'schedule': schedule,'tab':"adv"}))
    else:
        return redirect('login')


def accept(request, no):
    if request.session.has_key('username'):
        if request.method == "POST":
            q = adverts.objects.get(id=no)
            q.ad_status = 'Approved'
            q.save()
            return redirect('pending_for_approval')
        ad = adverts.objects.filter(id=no)
        schedule = adverts.objects.filter(ad_status='Approved', ad_date_from__gte=ad[0].ad_date_from,
                                          ad_date_from__lte=ad[0].ad_date_till).order_by('ad_date_from')
        return render(request, 'accept.html', ({'ad': ad, 'schedule': schedule,'tab':"adv"}))
    else:
        return redirect('login')


def reject(request, no):
    if request.session.has_key('username'):
        if request.method == "POST":
            desc = request.POST.get('desc')
            obj = rejected(ad_id=no, desc=desc)
            obj.save()
            q = adverts.objects.get(id=no)
            q.ad_status = 'Disapproved'
            q.save()
            return redirect('pending_for_approval')
        ad = adverts.objects.filter(id=no)
        return render(request, 'reject.html', ({'ad': ad,'tab':"adv"}))
    else:
        return redirect('login')


def view_rejected(request):
    if request.session.has_key('username'):
        reject = rejected.objects.raw("""SELECT * FROM mainactivity_adverts, mainactivity_rejected where 
            mainactivity_adverts.id=mainactivity_rejected.ad_id order by mainactivity_rejected.rej_date desc""")
        return render(request, 'view_rejected.html', ({'reject': reject,'tab':"adv"}))
    else:
        return redirect('login')


def pay_bills(request):
    if request.session.has_key('username'):
        cust = customer.objects.all()
        if request.method == 'POST':
            cust_id = request.POST.get('customer_id')
            bill = bills.objects.filter(cust_id=cust_id)
            sum = 0
            for i in bill:
                sum += i.total
            try:
                payment = payments.objects.get(cust_id=cust_id)
                amount_due = sum - payment.payment_amount
                amount_paid = payment.payment_amount
                payment_date = payment.payment_date
                payment_mode = payment.payment_mode
            except:
                amount_due = sum
                amount_paid = 0
                payment_date = "N/A"
                payment_mode = 'N/A'

            bi = bills.objects.values('ad_id', 'price', 'gst', 'total')
            ad = adverts.objects.values('id','cust_name','cust_id', 'ad_header', 'ad_date_from', 'ad_date_till', 'ad_page').filter(
                cust_id=cust_id)
            joined = join_tables(bi, ad)
            connected = conn(joined, "ad_id", "id")
            #bill = adverts.objects.raw("""Select * from mainactivity_adverts ad, mainactivity_bills bill where bill.ad_id=ad.id
             #    and ad.cust_id=%s""", [cust_id])

            return render(request, 'pay_bills.html', ({'bill': connected, 'cust': cust, 'amount_due': amount_due,
                                                      'amount_paid': amount_paid, 'payment_date': payment_date,
                                                       'payment_mode': payment_mode,'tab':"bills"}))
        return render(request, 'pay_bills.html', ({'cust': cust,'tab':"bills"}))
    else:
        return redirect('login')


def pay_confirm(request, no):
    if request.session.has_key('username'):
        if request.method == "POST":
            amount = request.POST.get('amount')
            mode = request.POST.get('mode')
            bill = bills.objects.filter(cust_id=no)
            sum = 0
            for i in bill:
                sum += i.total
            try:
                amount = float(amount)
                payment = payments.objects.get(cust_id=no)
                payment.payment_amount += amount
                payment.payment_due = sum - payment.payment_amount
                payment.payment_mode = mode
                payment.payment_date = datetime.datetime.now(tz=timezone.utc)
                if payment.payment_due < 1:
                    adverts.objects.filter(cust_id=no).filter(
                        Q(ad_status='Approved') | Q(ad_status='partially paid')).update(
                        ad_status='paid')
                    bills.objects.filter(cust_id=no).filter(
                        Q(bill_status='unpaid') | Q(bill_status='partially paid')).update(
                        bill_status='paid')

                else:
                    adverts.objects.filter(cust_id=no).filter(
                        Q(ad_status='Approved') | Q(ad_status='partially paid')).update(
                        ad_status='partially paid')
                    bills.objects.filter(cust_id=no).filter(
                        Q(bill_status='unpaid') | Q(bill_status='partially paid')).update(
                        bill_status='partially paid')
                payment.save()
            except:
                obj = payments(cust_id=no, payment_due=sum - float(amount), payment_amount=amount, payment_mode=mode)
                obj.save()
                if sum - float(amount) < 1:
                    adverts.objects.filter(cust_id=no).filter(
                        Q(ad_status='Approved') | Q(ad_status='partially paid')).update(
                        ad_status='paid')
                    bills.objects.filter(cust_id=no).filter(
                        Q(bill_status='unpaid') | Q(bill_status='partially paid')).update(
                        bill_status='paid')

                else:
                    adverts.objects.filter(cust_id=no).filter(
                        Q(ad_status='Approved') | Q(ad_status='partially paid')).update(
                        ad_status='partially paid')
                    bills.objects.filter(cust_id=no).filter(
                        Q(bill_status='unpaid') | Q(bill_status='partially paid')).update(
                        bill_status='partially paid')

            return redirect('pay_bills')
    else:
        return redirect('login')


def view_paid_bills(request):
    if request.session.has_key('username'):
        paid = rejected.objects.raw("""SELECT * FROM mainactivity_customer c, mainactivity_payments p where 
                c.cust_id=p.cust_id order by p.payment_date desc""")
        return render(request, 'view_paid_bills.html', ({'paid': paid,'tab':"bills"}))
    else:
        return redirect('login')
