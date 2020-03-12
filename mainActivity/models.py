from django.db import models

# Create your models here.
class customer (models.Model):
    cust_name=models.CharField(max_length=255)
    cust_address=models.CharField(max_length=255)
    cust_phone=models.CharField(max_length=15)
    cust_type=models.CharField(max_length=255)
    cust_id=models.CharField(max_length=30)
    cust_since=models.DateField()

    def __str__(self):
        return self.cust_name + " " + self.cust_type

class prices(models.Model):
    cust_type=models.CharField(max_length=255, unique=True)
    price=models.FloatField()

