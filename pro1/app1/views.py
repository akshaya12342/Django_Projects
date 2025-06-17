from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# home view
def home(request):
    return HttpResponse("Django")
def index(request):
    return HttpResponse("index")