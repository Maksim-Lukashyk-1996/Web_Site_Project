from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'Web_Site/index.html')

def Hello(request):
    return HttpResponse('<h1>Hello, have a nice day! :)</h1>')

def About_us(request):
    return render(request, 'Web_Site/about.html')
