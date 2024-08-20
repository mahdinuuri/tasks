from django.db import models
from datetime import date, timedelta

def get_default_duedate():
    return date.today() + timedelta(days=30)

class Members(models.Model):
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.name

class Opera(models.Model):
    task = models.CharField(max_length=200)
    duedate = models.DateField(default=get_default_duedate)
    description = models.CharField(max_length=500)
    duration = models.DurationField(default=timedelta(hours=1))
    priority = models.CharField(max_length=200)
    members = models.ManyToManyField(Members, related_name='operas')

    def __str__(self):
        return self.task

