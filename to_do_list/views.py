from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.db.models import F

from .forms import TaskForm

def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.all().update(priority = F('priority') + 1)
            newtask = Task(duration = form.cleaned_data['duration'],
            text=form.cleaned_data['text'], created=datetime.now())
            newtask.priority = 1
            newtask.save()
            return HttpResponseRedirect('/todolist/')
    else:
        form = TaskForm()
        tasks = Task.objects.all().order_by('priority')
        return render(request, 'to_do_list/index.html',
                     {'form': form, 'tasks': tasks}
        )

def deletetask(request, taskid):
        workingtask = Task.objects.get(id=taskid)
        if request.method == 'DELETE':
            workingtask.delete()
            #Can this operation be done on a queryset? How can it be enumerated?
            for index, task in enumerate(Task.objects.order_by('priority')):
                task.priority = index +1
                task.save()
        return HttpResponse(status=204)

def reorder(request):
    if request.method == 'POST':
        droppedItemPriority = request.POST.get('droppedItemPriority')
        droppedItemPosition = request.POST.get('droppedItemPosition')
        nextItemPriority = request.POST.get('nextItemPriority')
        previousItemPriority = request.POST.get('previousItemPriority')
        droppedtask = Task.objects.get(priority = droppedItemPriority)
        if previousItemPriority > droppedItemPriority:
            Task.objects.filter(priority__lte=previousItemPriority).filter(priority__gte=droppedItemPriority).update(priority = F('priority') -1)
        else:
            Task.objects.filter(priority__gte=nextItemPriority).filter(priority__lte=droppedItemPriority).update(priority = F('priority') +1)
        droppedtask.priority = droppedItemPosition
        droppedtask.save()
    return HttpResponse(status=202)
