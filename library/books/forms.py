
from django import forms

# form definition

# class BookForm(forms.Form):
#     title=forms.CharField()
#     author=forms.CharField()
#     price=forms.IntegerField()
#     pages=forms.IntegerField()
#     language_choices = [('english', 'English'), ('french', 'French'), ('malayalam', 'Malayalam'), ('hindi', 'Hindi')]
#     language=forms.ChoiceField(choices=language_choices)
#     image=forms.ImageField()


# using Modelform
from books.models import Book
class BookForm(forms.ModelForm):
    class Meta:  # inner class used to give description about form structure
        model=Book
        fields=['title','author','price','pages','language','image']
        # or
        # fields="__all__"
