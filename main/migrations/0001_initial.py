# Generated by Django 3.1 on 2020-08-13 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='criminalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(blank=True, max_length=120, null=True)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('record', models.TextField(blank=True, max_length=120, null=True)),
                ('level', models.CharField(choices=[('rl', 'Released'), ('wt', 'Wanted'), ('mw', 'Most Wanted')], default='rl', max_length=2)),
            ],
        ),
    ]