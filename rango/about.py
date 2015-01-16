from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says here is the about page.<br/> <a href='/rango'>Rango</a> This tutorial was put together by Thomas Robertson, 2081888")
