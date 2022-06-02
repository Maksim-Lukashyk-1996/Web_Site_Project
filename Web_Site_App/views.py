from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'Web_Site/index.html', {'title': 'Главная страница', 'tasks': tasks})

def About_us(request):
    return render(request, 'Web_Site/about.html')

def Create(request):
    return render(request, 'Web_Site/create.html')
