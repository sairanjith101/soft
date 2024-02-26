from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def admin(request):
    return HttpResponse("Hello Admin")

def guest(request, guest):
    return HttpResponse("Hello Guest " + guest)

def user(request, name):
    if name == 'admin':
        return HttpResponse(admin(request))
    else:
        return HttpResponse(guest(request, guest = name))