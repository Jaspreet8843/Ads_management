# Generated by Django 3.0.4 on 2020-03-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainActivity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rejected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_id', models.IntegerField()),
                ('desc', models.CharField(max_length=255)),
            ],
        ),
    ]
