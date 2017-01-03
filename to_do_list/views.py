from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from datetime import datetime

from .forms import TaskForm

def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            newtask = Task(duration = form.cleaned_data['duration'], text=form.cleaned_data['text'], created=datetime.now())
            newtask.save()
            return HttpResponseRedirect('/todolist/')
    else:
        form = TaskForm()
        tasks = Task.objects.all()
        return render(request, 'to_do_list/index.html', {'form': form, 'tasks': tasks})
