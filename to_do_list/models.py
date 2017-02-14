from django.db import models
from django.db.models import F


class Tasklist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.text

    def movetask(self, taskid, movedto):
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


class Task(models.Model):
    text = models.CharField(max_length=200)
    priority = models.IntegerField('priority', blank=True, null=True)
    duration = models.DurationField('estimated duration', blank=True, null=True)
    created = models.DateTimeField('date created')
    completed = models.DateTimeField('date completed', blank=True, null=True)
    tasklist = models.ForeignKey(Tasklist)
    current = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Starttask(models.Model):
    task = models.ForeignKey(Task)
    time = models.DateTimeField('time started')

class Stoptask(models.Model):
    task = models.ForeignKey(Task)
    time = models.DateTimeField('time stopped')
