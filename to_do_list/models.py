from django.db import models
from django.db.models import F


class Tasklist(models.Model):
    name = models.CharField(max_length=100)
    currenttask = models.OneToOneField(
    'Task', related_name="relatedtasklist", blank=True, null=True
     )

    def __unicode__(self):
        return self.name

    #takes task instead of taskid in to help prevent mid-air collisions
    def movetask(self, movedtask, movedto):
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

    def __unicode__(self):
        return self.text

class Juncture(models.Model):
    task = models.ForeignKey(Task)
    time = models.DateTimeField('time started')
    juncture_choices = (
    ('START', 'Start'),
    ('STOP', 'Stop')
    )
    juncture = models.CharField(max_length=5, choices=juncture_choices)
