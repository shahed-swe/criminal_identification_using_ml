# Generated by Django 3.1 on 2020-08-14 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminaldata',
            name='address',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='criminaldata',
            name='case_no',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='criminaldata',
            name='trace_no',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
