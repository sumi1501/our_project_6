from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def king(request):
    return HttpResponse('<h1>my inspration</h1>')