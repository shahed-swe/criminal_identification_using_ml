# Generated by Django 3.1 on 2020-08-15 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_criminaldata_phone'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='criminaldata',
            table='criminal_data',
        ),
    ]