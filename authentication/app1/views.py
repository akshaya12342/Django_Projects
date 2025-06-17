from tkinter.font import names

from django.contrib.auth.password_validation import password_changed
from django.db.transaction import commit
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

from django.views import View
from app1.forms import SignUpForm
from app1.forms import LoginForm

#  class based views using view class
class IndexView(View):
    def get(self,request):
        return render(request,'home.html')


class SignUpView(View):
    def post(self,request):  # after form submission
        form_instance=SignUpForm(request.POST)
        if(form_instance.is_valid()):
            # user=form_instance.save(commit=False) # when password need to saved encrypted format
            # #user.set_password(raw_data)
            # user.set_password(form_instance.cleaned_data['password'])
            #                                         # changes in the plaintext password format into encrypted format using Django SHA algorithm.
            #                                         # so here we call builtin function set_password()
            #
            # user.save()
             form_instance.save()
        return redirect('home')

    def get(self,request):
        form_instance=SignUpForm()
        return render(request,'signup.html',{'form':form_instance})


class SignInView(View):
    def get(self,request):
        form_instance=LoginForm()
        return render(request,'login.html',{'form':form_instance})
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if(form_instance.is_valid()):
            name=form_instance.cleaned_data['username']
            pwd=form_instance.cleaned_data['password']
            # print(name,pwd)
            user=authenticate(username=name,password=pwd)
            # if username and password is valid "user" returns user object if exist or returns none
            if user:
                # starting session using current session
                login(request, user) # adds the current user to the session
                # u=request.user
                # print(u.name) # prints the current username of the user who has login recently/currently
                # print(u.email)
                # print(u.first_name)
                return redirect('login')
            else:
                print("Invalid User credentials")
        return redirect('home')


class SignOutView(View):
    def get(self,request):
        logout(request)
        return redirect('signin')

