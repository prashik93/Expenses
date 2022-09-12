from django.contrib import admin
from .models import ExpenseTable

# Register your models here.
class ExpenseTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'amount', 'date']

admin.site.register(ExpenseTable, ExpenseTableAdmin)