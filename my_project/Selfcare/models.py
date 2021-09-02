from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Articles(models.Model):
    Name = models.CharField(default='Self care', max_length=400)
    article = models.URLField(max_length=400)

    def __str__(self):
        return self.Name


class Tasks(models.Model):
    tasks = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.tasks


class Challengers(models.Model):
    Challenge = models.CharField(max_length=500)
    Why = models.TextField(max_length=2000)

    def __str__(self):
        return self.Challenge


class stressbusters(models.Model):
    Problem = models.CharField(max_length=500)
    Why = models.TextField(max_length=500)
    Avoid = models.TextField(max_length=500)
    Fix = models.TextField(max_length=1000)

    def __str__(self):
        return self.Problem


# routine
class morning(models.Model):
    text = RichTextField(max_length=10000)

    def __str__(self):
        return self.text

class workout(models.Model):
    text = RichTextField(max_length=10000)

    def __str__(self):
        return self.text

class study(models.Model):
    text = RichTextField(max_length=10000)

    def __str__(self):
        return self.text

class diet(models.Model):
    text = RichTextField(max_length=10000)

    def __str__(self):
        return self.text

class skincare(models.Model):
    text = RichTextField(max_length=10000)

    def __str__(self):
        return self.text

class night(models.Model):
    text = RichTextField(max_length=10000)

    def __str__(self):
        return self.text

class detox(models.Model):
    text = RichTextField(max_length=10000)

    def __str__(self):
        return self.text
