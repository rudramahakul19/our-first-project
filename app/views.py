from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def jampandu(request):
    return HttpResponse("hi jam pandu how are yoy")

def rudra(request):
    return HttpResponse("hi rudra how are yoy")
