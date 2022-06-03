from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

from .forms import TaskForm

def index(request):
    if request.method == 'POST':
        error = ''
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Неверная форма'
    tasks = Task.objects.order_by('-id')
    return render(request, 'Web_Site/index.html', {'title': 'Главная страница', 'tasks': tasks})

def About_us(request):
    return render(request, 'Web_Site/about.html')

def Create(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'Web_Site/create.html', context)

def Delete(request):
    return render(request, 'Web_Site/delete.html')
