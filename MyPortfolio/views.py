from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio
from math import ceil
# Create your views here.
def index(request):
    portfolio = Portfolio.objects.all()
    n = len(portfolio)
    nslides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slide':nslides,'range':range(1,nslides),'portfolio':portfolio}
    return render(request,'MyPortfolio/index.html',params)