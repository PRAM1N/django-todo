from django.db import models

# Create your models here.

class Todo(models.Model):  #class-based models
   name=models.CharField(max_length=50)
   description=models.TextField()
   status=models.CharField(max_length=50)