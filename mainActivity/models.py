from django.db import models

# Create your models here.
class customer (models.Model):
    cust_name=models.CharField(max_length=255)
    cust_address=models.CharField(max_length=255)
    cust_phone=models.CharField(max_length=255)
    cust_type=models.CharField(max_length=255)
    cust_id=models.CharField(max_length=255, unique=True)
    cust_since=models.DateField()

    # def __str__(self):
    #     return self.cust_name + " " + self.cust_type

class prices(models.Model):
    cust_type=models.CharField(max_length=255, unique=True)
    price=models.FloatField()

class adverts(models.Model):
    cust_name=models.CharField(max_length=255)
    cust_id=models.CharField(max_length=255)
    ad_header=models.CharField(max_length=255)
    ad_date_from=models.DateField()
    ad_date_till=models.DateField()
    ad_status=models.CharField(max_length=255, default="Pending for approval")
    ad_height=models.CharField(max_length=255)
    ad_width=models.CharField(max_length=255)
    ad_page=models.CharField(max_length=255)

class rejected(models.Model):
    ad_id=models.IntegerField()
    desc=models.CharField(max_length=255)

class bills(models.Model):
	cust_id=models.CharField(max_length=255)
	ad_id=models.IntegerField(unique=True)
	price=models.FloatField()
	gst=models.FloatField()
	total=models.FloatField()
	billing_date=models.DateField()
	bill_status=models.CharField(max_length=255, default="unpaid")


