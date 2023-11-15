from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_fell(request):
    return HttpResponse('<h1> Hello Fell </h1>')