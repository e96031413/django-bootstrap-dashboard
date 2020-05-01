import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt

# Create your views here.

def login(request):
    return render (request,'login.html')

def index(request):
    return render (request,'index.html')

def MDT(request):
    return render (request,'Master-Detail-Table.html')

def MDT_2(request):
    return render (request,'Master-Detail-Table-2.html')

def MDDTable(request):
    return render (request,'M-D-D-Table.html')

def SingleTable(request):
    return render (request,'Single-Table.html')

def SingleTable_2(request):
    return render (request,'Single-Table-2.html')