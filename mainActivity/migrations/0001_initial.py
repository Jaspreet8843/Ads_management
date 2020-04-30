# Generated by Django 3.0.2 on 2020-04-28 04:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adverts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=255)),
                ('cust_id', models.CharField(max_length=255)),
                ('ad_header', models.CharField(max_length=255)),
                ('ad_date_from', models.DateField()),
                ('ad_date_till', models.DateField()),
                ('ad_status', models.CharField(default='Pending for approval', max_length=255)),
                ('ad_height', models.CharField(max_length=255)),
                ('ad_width', models.CharField(max_length=255)),
                ('ad_page', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.CharField(max_length=255)),
                ('ad_id', models.IntegerField(unique=True)),
                ('price', models.FloatField()),
                ('gst', models.FloatField()),
                ('total', models.FloatField()),
                ('billing_date', models.DateField()),
                ('bill_status', models.CharField(default='unpaid', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=255)),
                ('cust_address', models.CharField(max_length=255)),
                ('cust_phone', models.CharField(max_length=255)),
                ('cust_type', models.CharField(max_length=255)),
                ('cust_id', models.CharField(max_length=255, unique=True)),
                ('cust_since', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.CharField(max_length=255)),
                ('payment_due', models.FloatField()),
                ('payment_amount', models.FloatField()),
                ('payment_mode', models.CharField(max_length=255)),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_type', models.CharField(max_length=255, unique=True)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='rejected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_id', models.IntegerField()),
                ('desc', models.CharField(max_length=255)),
                ('rej_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255, unique=True)),
                ('user_pass', models.CharField(max_length=255)),
            ],
        ),
    ]