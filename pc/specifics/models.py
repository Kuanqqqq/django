from django.db import models
from django.db.models.base import Model

# Create your models here.
class Memory(models.Model):
    capacity = models.CharField(max_length=50)

    def __str__(self):
        return self.capacity

