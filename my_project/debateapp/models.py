from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    #point = models.TextField()
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
class textbox_model(models.Model):
    Poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
    body = models.TextField(max_length = 5000 , null=False,blank=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.body
