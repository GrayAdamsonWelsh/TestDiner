from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def menu(request):
    return HttpResponse("Hello, Menu!")
