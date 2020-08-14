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
    address = forms.CharField(max_length=120,widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'address',
        'placeholder':'Enter Criminal Address',
    }))
    phone = forms.CharField(max_length=120,widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'phone',
        'placeholder':'Enter Criminal Phone Number',
    }))
    case_no = forms.CharField(max_length=120,widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'case_no',
        'placeholder':'Enter Criminal Case Number',
    }))
    trace_no = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'trace_no',
        'placeholder':'Enter Criminal Trace Number',
    }))
    record = forms.CharField(max_length=120, widget=forms.Textarea(attrs={
        'class':'form-control',
        'id':'trace_no',
        'placeholder':'Enter Criminal Record',
        'rows':'5',
        'cols':'20',
    }))
    level = forms.CharField(max_length=120, widget=forms.Select(attrs={
        'class':'form-control',
        'id':'level',
    },choices=levels))

    class Meta:
        model = criminalData
        fields = ['cid','name','address','phone','case_no','trace_no','record','level']
