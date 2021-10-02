from django.db import models
from django.db.models.base import Model
from colorfield.fields import ColorField
# Create your models here.
class Memory(models.Model):
    capacity = models.CharField(max_length=50)

    def __str__(self):
        return self.capacity


class Color(models.Model):
    color = ColorField(format='hexa')

    def __str__(self):
        return self.color
