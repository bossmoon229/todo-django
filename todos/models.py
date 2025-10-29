from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

# Create your models here.

def get_default_deadline():
    return date.today() + timedelta(days=1)

class Todo(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=10)
    description = models.TextField(max_length=100)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        choices=[
            ('todo', 'To do'), 
            ('in_progress', 'In progress'), 
            ('done', 'Done')], default='todo')
    deadline = models.DateField(default=get_default_deadline)
    priority = models.CharField(
        choices=[
            ('low', 'Low'), 
            ('medium', 'Medium'), 
            ('high', 'High')], default='low')

    def __str__(self):
        return self.title

