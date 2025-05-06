from typing import Self
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
    position = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name