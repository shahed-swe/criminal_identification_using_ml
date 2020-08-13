from django.db import models

# Create your models here.
class criminalData(models.Model):
    levels = [
        ('rl','Released'),
        ('wt','Wanted'),
        ('mw','Most Wanted'),
    ]
    cid = models.CharField(max_length=120,blank=True,null=True)
    name = models.CharField(max_length=120,blank=True, null=True)
    record = models.TextField(max_length=120,blank=True, null=True)
    level = models.CharField(max_length=2,choices=levels,default='rl')