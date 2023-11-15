from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    a ='hi'
    return HttpResponse(f'<h1> Hello gs3 {a}, i am gs3 </h1>')