from django.db import models

class Tasklist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.text

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
