from django.contrib import admin
from MoneyMatters.models import Savings, Debts, MTG, Expenses, Income

# Register your models here.
admin.site.register(Savings)
admin.site.register(Debts)
admin.site.register(MTG)
admin.site.register(Expenses)
admin.site.register(Income)
