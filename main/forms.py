from django import forms
from .models import criminalData

class DataForm(forms.ModelForm):
    levels = [
        ('rl', 'Released'),
        ('wt', 'Wanted'),
        ('mw', 'Most Wanted'),
    ]
    cid = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'cid',
        'placeholder':'Enter Criminal id',
    }))
    name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'name',
        'placeholder':'Enter Criminal Name',
    }))
    record = forms.CharField(max_length=120, widget=forms.Textarea(attrs={
        'class':'form-control',
        'id':'record',
        'placeholder':'Enter Criminal Record',
    }))
    level = forms.CharField(max_length=120, widget=forms.Select(attrs={
        'class':'form-control',
        'id':'level',
    },choices=levels))

    class Meta:
        model = criminalData
        fields = ['cid','name','record','level']
