

from django import forms
from django.forms import PasswordInput


class AdditionForm(forms.Form):
    number1=forms.IntegerField()
    number2=forms.IntegerField()

class FactForm(forms.Form):
    number1 = forms.IntegerField()

class BmiForm(forms.Form):
    height=forms.IntegerField()
    weight=forms.IntegerField()

class signupForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50,widget=PasswordInput)
    email=forms.EmailField()
    gender_choices=[('male',"Male"),('female',"Female")]
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
    role_choices=[('admin',"Admin"),('student',"Student")]
    role=forms.ChoiceField(choices=role_choices)

class calorieForm(forms.Form):
    gender_choices = [('male', "Male"), ('female', "Female")]
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)
    height=forms.IntegerField()
    weight=forms.IntegerField()
    age=forms.IntegerField()
    activity_choices = [(1.2,'sedentary'),(1.375,'lightly active'),
                        (1.55,'moderately active'),(1.75,'very active'),
                        (1.9,'extra active')]
    activity= forms.ChoiceField(choices=activity_choices)

