from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.utils import timezone
from django.db.models import F

from .forms import TaskForm


def todolist(request, tasklistid):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.update(priority = F('priority') + 1)
            newtask = Task(duration = form.cleaned_data['duration'],
            text=form.cleaned_data['text'], created=timezone.now())
            newtask.priority = 1
            newtask.tasklist_id=tasklistid
            newtask.save()
            return HttpResponseRedirect('/todolist/' + tasklistid)
    else:
        form = TaskForm()
        thislist = Tasklist.objects.get(id=tasklistid)
        currenttask = thislist.currenttask
        tasks = Task.objects.filter(tasklist=tasklistid, completed__isnull=True
        ).order_by('priority')
        finishedtasks = Task.objects.exclude(tasklist=tasklistid, completed__isnull=True
        ).order_by('priority')
        return render(request, 'to_do_list/index.html',
                     {'form': form,
                     'tasks': tasks,
                     'finishedtasks': finishedtasks,
                     'tasklist': thislist,
                     'currenttask': currenttask
                     }
        )

def reports(request, tasklistid):
    tasklist = Tasklist.objects.get(id=tasklistid)
    tasks = Task.objects.filter(tasklist=tasklistid, completed__isnull=False)
    print(tasks)
    return render(request, 'to_do_list/reports.html',
                 {'tasklist': tasklist,
                  'tasks': tasks
                  }
                 )

def deletetask(request, taskid):
    if request.method == 'DELETE':
        workingtask = Task.objects.get(id=taskid)
        priority = workingtask.priority
        workingtask.delete()
        Task.objects.filter(priority__gte=priority).update(
            priority = F('priority')-1)
    return HttpResponse(status=204)

def reorder(request, tasklistid):
    if request.method == 'POST':
        taskid = request.POST.get('taskid')
        task = Task.objects.get(id=taskid)
        movedto = int(request.POST.get('movedto'))
        tasklist = Tasklist.objects.get(id=tasklistid)
        tasklist.movetask(task, movedto)
    return HttpResponse(status=202)

def updatetask(request):
    if request.method == 'POST':
        updatetype = request.POST.get('updatetype')
        taskid = request.POST.get('taskid')
        task = Task.objects.get(id=taskid)
        tasklist = task.tasklist
        if updatetype == 'workontask':
            tasklist.movetask(task, 1)
            tasklist.currenttask = task
            juncture = Juncture(
                task=task,
                time=timezone.now(),
                juncture='START'
                )
        else:
            tasklist.currenttask = None
            if updatetype == 'finishtask':
                task.completed = timezone.now()
                task.save()
            juncture = Juncture(
                task=task,
                time=timezone.now(),
                juncture='STOP'
                )
        tasklist.save()
        juncture.save()
    return HttpResponseRedirect('/todolist/' + str(tasklist.id))
