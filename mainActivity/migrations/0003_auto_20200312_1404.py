# Generated by Django 3.0.4 on 2020-03-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainActivity', '0002_auto_20200309_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cust_type',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]