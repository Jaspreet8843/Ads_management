from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(customer)
admin.site.register(prices)
admin.site.register(payments)
admin.site.register(bills)
admin.site.register(adverts)
admin.site.register(rejected)
admin.site.register(users)
