from django.db import models

# Create your models here.

class Todo(models.Model):
    user_name= models.CharField(max_length=10)
    title = models.CharField(max_length=10)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.title
