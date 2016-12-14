from __future__ import unicode_literals

from django.db import models

class Task(models.Model):
    text = models.CharField(max_length=200)
    created = models.DateTimeField('date created')
    completed = models.DateTimeField('date completed', blank=True, null=True)

class Starttask(models.Model):
    task = models.ForeignKey(Task)
    time = models.DateTimeField('time started')

class Stoptask(models.Model):
    task = models.ForeignKey(Task)
    time = models.DateTimeField('time stopped')


# Create your models here.
