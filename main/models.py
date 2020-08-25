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
    address = models.CharField(max_length=120,blank=True, null=True)
    phone = models.CharField(max_length=120,blank=True,null=True)
    case_no = models.CharField(max_length=120, blank=True, null=True)
    trace_no = models.CharField(max_length=120,blank=True, null=True)
    record = models.TextField(max_length=120,blank=True, null=True)
    level = models.CharField(max_length=2,choices=levels,default='rl')

    class Meta:
        db_table = 'criminal_data'