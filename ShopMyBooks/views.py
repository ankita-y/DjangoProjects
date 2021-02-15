from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):

    product = Product.objects.all()
    n = len(product)
    nslides = n//4 + ceil((n/4)-(n//4))
    allproducts = [[product, range(1,nslides),nslides],
    [product, range(1,nslides),nslides]]
    # params = {'no_of_slide':nslides,'range':range(1,nslides),'product':product}
    params = {'allproducts':allproducts}
    return render(request,'index.html',params)

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