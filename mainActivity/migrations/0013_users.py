# Generated by Django 3.0.4 on 2020-04-28 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainActivity', '0012_auto_20200325_1328'),
    ]

    operations = [
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