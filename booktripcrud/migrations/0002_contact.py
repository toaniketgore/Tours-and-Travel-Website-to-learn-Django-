# Generated by Django 4.1 on 2022-09-26 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktripcrud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('sNO', models.AutoField(primary_key=True, serialize=False)),
                ('customerName', models.CharField(default='customer-name', max_length=50)),
                ('customerEmail', models.EmailField(default='customer-name', max_length=50)),
                ('customerPhone', models.IntegerField(default='customer-phonenumber', max_length=12)),
                ('customerAddress', models.CharField(default='customer-address', max_length=300)),
                ('customerWhereTo', models.CharField(default='customer-wheretoplace', max_length=50)),
                ('customerNoOfGuests', models.IntegerField(default='customer-NoOfGuests', max_length=1000)),
                ('customerArrivalDate', models.DateField()),
                ('customerLeavingDate', models.DateField()),
            ],
        ),
    ]