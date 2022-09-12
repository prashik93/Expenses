from django.db import models

# Create your models here.

class ExpenseTable(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32)
    amount = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return 'Id = {}, Title = {}, Amount = {}, Date = {}'.format(self.id, self.title, self.amount, self.date)