from django.db import models


# Create your models here.
class Savings(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    amount = models.FloatField(max_length=10)

    @property
    def __str__(self):
        return self.title


class Debts(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    amount = models.FloatField(max_length=7)
    due = models.DateField(default='mm/dd/yy')

    @property
    def __str__(self):
        return self.title


class MTG(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    amount = models.FloatField(max_length=10)

    @property
    def __str__(self):
        return self.title


class Expenses(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    amount = models.FloatField(max_length=7)

    @property
    def __str__(self):
        return self.title


class Income(models.Model):
    income = models.FloatField(max_length=7)
    def __str__(self):
        return str(self.income)
