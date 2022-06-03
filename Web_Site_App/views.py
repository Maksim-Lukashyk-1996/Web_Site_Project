from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from django.views.generic import DeleteView

from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'Web_Site/index.html', {'title': 'Главная страница', 'tasks': tasks})

def About_us(request):
    return render(request, 'Web_Site/about.html')

def Create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'Web_Site/create.html', context)

class DeleteView(DeleteView):
    model = Task
    success_url = 'home'
    template_name = 'Web_Site/delete.html'