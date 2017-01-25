from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.utils import timezone
from django.db.models import F

from .forms import TaskForm

def movetask(taskid, movedto):
    for task in Task.objects.all():
        print("{},{},{}").format(task.text, task.id, task.priority)
    print("taskid = {}").format(taskid)
    print("movedto = {}").format(movedto)
    movedtask = Task.objects.get(id=taskid)
    if movedtask.priority > movedto:
        Task.objects.filter(priority__gte=movedto).filter(
            priority__lte=movedtask.priority).update(
                priority = F('priority') +1)
    else:
        Task.objects.filter(priority__lte=movedto).filter(
            priority__gte=movedtask.priority).update(
                priority = F('priority') -1)
    movedtask.priority = movedto
    movedtask.save()
    for task in Task.objects.all():
        print("{},{},{}").format(task.text, task.id, task.priority)

def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.all().update(priority = F('priority') + 1)
            newtask = Task(duration = form.cleaned_data['duration'],
            text=form.cleaned_data['text'], created=timezone.now())
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
        if request.method == 'DELETE':
            workingtask = Task.objects.get(id=taskid)
            priority = workingtask.priority
            workingtask.delete()
            Task.objects.filter(priority__gte=priority).update(
                priority = F('priority')-1)
        return HttpResponse(status=204)

def reorder(request):
    if request.method == 'POST':
        taskid = request.POST.get('taskid')
        movedto = request.POST.get('movedto')
        movetask(taskid, movedto)
    return HttpResponse(status=202)
