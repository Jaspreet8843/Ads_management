# Generated by Django 3.0.4 on 2020-03-25 05:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainActivity', '0010_auto_20200324_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='ad_id',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='bill_id',
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 25, 5, 44, 51, 298424, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rejected',
            name='rej_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 25, 5, 44, 51, 85411, tzinfo=utc)),
        ),
    ]