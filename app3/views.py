from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample3(request,name):
    return HttpResponse(f'<h1>you entered {name}</h1>')
