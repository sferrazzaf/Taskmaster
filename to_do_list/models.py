from __future__ import unicode_literals
from django.db.models import F

from django.db import models

class Tasklist(models.Model):
    name = models.CharField(max_length=100)

class Task(models.Model):
    text = models.CharField(max_length=200)
    priority = models.IntegerField('priority', blank=True, null=True)
    duration = models.DurationField('estimated duration', blank=True, null=True)
    created = models.DateTimeField('date created')
    completed = models.DateTimeField('date completed', blank=True, null=True)
    tasklist = models.ForeignKey(Tasklist)

    def __str__(self):
        return self.text

class Currenttask(models.Model):
    task = models.ForeignKey(Task, blank=True, null=True)
    tasklist = models.ForeignKey(Tasklist)

class Starttask(models.Model):
    task = models.ForeignKey(Task)
    time = models.DateTimeField('time started')
    tasklist = models.ForeignKey(Tasklist)

class Stoptask(models.Model):
    task = models.ForeignKey(Task)
    time = models.DateTimeField('time stopped')
    tasklist = models.ForeignKey(Tasklist)
