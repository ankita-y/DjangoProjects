from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'Aboutus.html')

def contactus(request):
    return HttpResponse("This is contactus")

def myorder(request):
    return HttpResponse("This is myorder")

def search(request):
    return HttpResponse("This is search")

def productview(request):
    return HttpResponse("This is product")

def checkout(request):
    return HttpResponse("This is checkout")