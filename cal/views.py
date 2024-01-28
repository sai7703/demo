from django.shortcuts import render
from django.http import HttpResponse
def member(request):
    str1="<h1 style='color:red'>bharath</h1>"
    return HttpResponse(str1)

# Create your views here.
