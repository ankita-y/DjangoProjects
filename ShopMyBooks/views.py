from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):

    product = Product.objects.all()
    return render(request,'index.html',{'product': product})

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