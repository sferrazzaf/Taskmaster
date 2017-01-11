from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from datetime import datetime

from .forms import TaskForm

def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            newtask = Task(duration = form.cleaned_data['duration'],
            text=form.cleaned_data['text'], created=datetime.now())
            newtask.save()
            return HttpResponseRedirect('/todolist/')
    else:
        form = TaskForm()
        tasks = Task.objects.all().order_by('priority')
        return render(request, 'to_do_list/index.html',
                     {'form': form, 'tasks': tasks}
        )

def reorder(request):
    if request.method == 'POST':
        droppedItemPriority = request.POST.get('droppedItemPriority')
        droppedItemPosition = request.POST.get('droppedItemPosition')
        nextItemPriority = request.POST.get('nextItemPriority')
        nextItemPosition = request.POST.get('nextItemPosition')
        previousItemPriority = request.POST.get('previousItemPriority')
        previousItemPosition = request.POST.get('previousItemPosition')
        print(nextItemPosition)
        print(nextItemPriority)
        print(previousItemPosition)
        print(previousItemPriority)
    return HttpResponse("blarg!")
