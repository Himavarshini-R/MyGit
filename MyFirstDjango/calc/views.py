# Create your views here.
from django.shortcuts import render
def home(request):
 return render(request,'home.html',{'name':'Varshi'})
def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=val1+val2
    return render(request,'result.html',{'result':val3})