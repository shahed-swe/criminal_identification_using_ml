from django import forms
from .models import criminalData
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

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





class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'user_field',
            'placeholder': 'Enter Your Username',
        }
    ))
    first_name = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'first_name',
            'placeholder': 'Enter Your First Name',
        }
    ))
    last_name = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'last_name',
            'placeholder': 'Enter Your Last Name',
        }
    ))

    email = forms.CharField(max_length=120, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'id': 'email_field',
            'placeholder': 'Enter Your Email'
        }
    ))
    password1 = forms.CharField(max_length=12, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password_field_one',
            'placeholder': 'Enter Password First',
        }
    ))
    password2 = forms.CharField(max_length=12, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password_field_two',
            'placeholder': 'Enter Password Again',
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def check_duplicate_user_name(self, *args, **kwargs):
        instance = self.instance
        username = self.cleaned_data.get('username')
        check = User.objects.filter(username__iexact=username)
        if instance is not None:
            check = check.exclude(pk=instance.pk)
        if check.exists():
            raise forms.ValidationError("User is already exists")
        return username

    def email_validation_check(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        data = validate_email(email)
        if data != True:
            raise forms.ValidationError("Enter corrent email address")
        return email

    def password_validation_check(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Password Does not match")
        return password1
