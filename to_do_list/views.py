from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.utils import timezone
from django.db.models import F

from .forms import TaskForm

def movetask(taskid, movedto):
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

def todolist(request, tasklist):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.all().update(priority = F('priority') + 1)
            newtask = Task(duration = form.cleaned_data['duration'],
            text=form.cleaned_data['text'], created=timezone.now())
            newtask.priority = 1
            newtask.tasklist_id=tasklist
            newtask.save()
            return HttpResponseRedirect('/todolist/' + tasklist)
    else:
        form = TaskForm()
        thislist = Tasklist.objects.get(id=tasklist)
        currenttask = Task.objects.filter(tasklist=thislist.id).filter(current=True)
        if not currenttask:
            currenttask = "None"
        tasks = Task.objects.filter(tasklist=tasklist).order_by('priority')
        return render(request, 'to_do_list/index.html',
                     {'form': form,
                     'tasks': tasks,
                     'tasklist': thislist,
                     'currenttask': currenttask
                     }
        )

def deletetask(request, tasklist, taskid):
        if request.method == 'DELETE':
            workingtask = Task.objects.get(id=taskid)
            priority = workingtask.priority
            workingtask.delete()
            Task.objects.filter(priority__gte=priority).update(
                priority = F('priority')-1)
        return HttpResponse(status=204)

def reorder(request, tasklist):
    if request.method == 'POST':
        taskid = request.POST.get('taskid')
        movedto = int(request.POST.get('movedto'))
        movetask(taskid, movedto)
    return HttpResponse(status=202)

def togglecurrent(request, tasklistid):
    if request.method =='POST':
        currenttasklist = Tasklist.objects.get(id=tasklistid)
        taskid = request.POST.get('taskid')
        currenttask = Task.objects.get(id=taskid)
        Task.objects.filter(tasklist=currenttasklist).update(current=False)
        currenttask.current = True
        currenttask.save()
    return HttpResponse(status=202)
