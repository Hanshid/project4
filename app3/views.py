from django.shortcuts import render

# Create your views here.
from django.urls import path
from . import views
def testfun(request):
   return render(request,'login.html')
   return render(request,'login1.html')