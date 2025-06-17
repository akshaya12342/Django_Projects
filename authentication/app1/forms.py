

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# class SignUpForm(forms.ModelForm):
#     password1=forms.CharField() # confirm password
#     class Meta:
#         model=User
#         fields=['username','password','email','first_name','last_name','password1']


class SignUpForm(UserCreationForm):
    class Meta:
        model=User   # table name for record creation
        fields=['username','password1','password2','email','first_name','last_name']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()