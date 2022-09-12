from rest_framework import serializers
from .models import ExpenseTable

class ExpenseTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseTable
        fields = ['id', 'title', 'amount', 'date']