from django.db import models
import datetime

class Task(models.Model):

    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    Deadline = models.DateField(default=datetime.date.today)
    color = models.CharField(max_length=7, null=True)



    def __str__(self):
        return self.title
