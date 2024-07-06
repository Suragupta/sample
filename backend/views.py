from django.shortcuts import render,redirect
from backend.models import *
from django.http import HttpResponse 
# Create your views here.

def homeVw(request):
        return render(request,"index.html")