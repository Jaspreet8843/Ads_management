from django.db.models import Q
import datetime
from django.shortcuts import render, redirect
from .models import customer, prices, adverts, rejected, bills, payments
from django.utils import timezone
import time


# Create your views here.

def index(request):
    # c=customer.objects.filter(cust_type="govt")
    # p=prices(cust_type=c[0], price='10000')
    return render(request, 'localsdirectory/index.html',({'tab':"home"}))


# PRICES--------------------------------------------------------------------------------
def view_prices(request):
    p = prices.objects.all()
    return render(request, 'view_prices.html', ({'prices': p}))


def edit_prices(request):
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


def delete(request, no):
    p = prices.objects.filter(id=no).delete()
    return redirect(edit_prices)


# CUSTOMER-------------------------------------------------------------------------------
def add_customer(request):
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


def view_customers(request):
    cust = customer.objects.all()
    return render(request, 'view_customers.html', ({'customers': cust,'tab':"customers"}))


# ADVERTISEMENTS----------------------------------------------------------------------------
def add_advert(request):
    if request.method == 'POST':
        cust_name = request.POST.get('customer_name')
        cust_id = request.POST.get('customer_id')
        dis_from = request.POST.get('disp_from')
        dis_till = request.POST.get('disp_till')
        ad_header = request.POST.get('ad_header')
        ad_height = request.POST.get('ad_height')
        ad_width = request.POST.get('ad_width')
        ad_page = request.POST.get('ad_page')
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
    cust = {}
    cust_obj = customer.objects.all()
    cust_name = []
    cust_id = []
    for c in cust_obj:
        cust_name.append(c.cust_name)
        cust_id.append(c.cust_id)
    cust['name'] = cust_name
    cust['id'] = cust_id
    cust['tab'] = "adv"
    return render(request, 'add_advert.html', (cust))


def view_adverts(request):
    ads = adverts.objects.all()
    return render(request, 'view_adverts.html', ({'advertisements': ads,'tab':"adv"}))



#BILLING---------------------------------------------------------------------------------
def billing(request):
    cust = customer.objects.filter()
    if request.method == 'POST':
        cust_id = request.POST.get('customer_id')
        ads = adverts.objects.filter(cust_id=cust_id, ad_status="Approved").order_by('ad_date_from')
        ads = ads.exclude(id__in=bills.objects.filter(cust_id=cust_id).values('ad_id'))
        return render(request, 'billing.html', ({'cust': cust, 'ads': ads, 'customer_id': cust_id,'tab':"bills"}))
    return render(request, 'billing.html', ({'cust': cust,'tab':"bills"}))


def view_bills(request):
    cust = customer.objects.filter()
    if request.method == 'POST':
        cust_id = request.POST.get('customer_id')
        bill = adverts.objects.raw("""Select * from mainactivity_adverts ad, mainactivity_bills bill where bill.ad_id=ad.id
         and ad.cust_id=%s""", [cust_id])
        return render(request, 'view_bills.html', ({'bill': bill, 'cust': cust,'tab':"bills"}))
    return render(request, 'view_bills.html', ({'cust': cust,'tab':"bills"}))


def store_bills(request, cust_id):
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


def view_schedule(request):
    schedule = ''
    if request.method == "POST":
        date_from = request.POST.get('from')
        date_upto = request.POST.get('upto')
        if date_from != '' or date_upto != '':
            schedule = adverts.objects.filter(ad_date_from__gte=date_from, ad_date_from__lte=date_upto).order_by(
                'ad_date_from')
        else:
            schedule = adverts.objects.all().order_by('ad_date_from')
    return render(request, 'view_schedule.html', ({'schedule': schedule,'tab':"schedule"}))


def pending_for_approval(request):
    schedule = adverts.objects.filter(ad_status='Pending for approval').order_by('ad_date_from')
    return render(request, 'pending_for_approval.html', ({'schedule': schedule,'tab':"adv"}))


def accept(request, no):
    if request.method == "POST":
        q = adverts.objects.get(id=no)
        q.ad_status = 'Approved'
        q.save()
        return redirect('pending_for_approval')
    ad = adverts.objects.filter(id=no)
    schedule = adverts.objects.filter(ad_status='Approved', ad_date_from__gte=ad[0].ad_date_from,
                                      ad_date_from__lte=ad[0].ad_date_till).order_by('ad_date_from')
    return render(request, 'accept.html', ({'ad': ad, 'schedule': schedule,'tab':"adv"}))


def reject(request, no):
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


def view_rejected(request):
    reject = rejected.objects.raw("""SELECT * FROM mainactivity_adverts, mainactivity_rejected where 
        mainactivity_adverts.id=mainactivity_rejected.ad_id order by mainactivity_rejected.rej_date desc""")
    return render(request, 'view_rejected.html', ({'reject': reject,'tab':"adv"}))


def pay_bills(request):
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

        bill = adverts.objects.raw("""Select * from mainactivity_adverts ad, mainactivity_bills bill where bill.ad_id=ad.id
             and ad.cust_id=%s""", [cust_id])
        return render(request, 'pay_bills.html', ({'bill': bill, 'cust': cust, 'amount_due': amount_due,
                                                   'amount_paid': amount_paid, 'payment_date': payment_date,
                                                   'payment_mode': payment_mode,'tab':"bills"}))
    return render(request, 'pay_bills.html', ({'cust': cust,'tab':"bills"}))


def pay_confirm(request, no):
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


def view_paid_bills(request):
    paid = rejected.objects.raw("""SELECT * FROM mainactivity_customer c, mainactivity_payments p where 
            c.cust_id=p.cust_id order by p.payment_date desc""")
    return render(request, 'view_paid_bills.html', ({'paid': paid,'tab':"bills"}))
