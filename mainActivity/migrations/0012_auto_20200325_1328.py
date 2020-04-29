# Generated by Django 3.0.4 on 2020-03-25 07:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainActivity', '0011_auto_20200325_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='rejected',
            name='rej_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
