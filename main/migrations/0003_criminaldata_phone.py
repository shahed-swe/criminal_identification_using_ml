# Generated by Django 3.1 on 2020-08-14 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200814_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminaldata',
            name='phone',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]