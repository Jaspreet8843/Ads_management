# Generated by Django 3.0.2 on 2020-03-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainActivity', '0007_auto_20200312_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cust_address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='cust_id',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='cust_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='cust_phone',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
