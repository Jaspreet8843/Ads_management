# Generated by Django 3.0.4 on 2020-03-24 06:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainActivity', '0005_auto_20200324_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rejected',
            name='rej_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 6, 18, 9, 365969, tzinfo=utc)),
        ),
    ]
