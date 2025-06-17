

from django import forms
from django.contrib.auth.forms import UserCreationForm

# class SignUpForm(forms.ModelForm):
#     password1=forms.CharField() # confirm password
#     class Meta:
#         model=User
#         fields=['username','password','email','first_name','last_name','password1']

from app1.models import CustomUser
class SignUpForm(UserCreationForm):
    class Meta:
        model=CustomUser   # table name for record creation
        fields=['username','password1','password2','email','first_name','last_name','phone','address']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()