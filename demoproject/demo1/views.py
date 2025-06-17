
from django.shortcuts import render
def home(request):
     context={'name':'arun','age':25,'place':'ekm'}
     return render(request,'home.html')
# Create your views here.
     def first(request):
         return render(request,'first.html')

    def second(request):
         return render(request,'second.html')
