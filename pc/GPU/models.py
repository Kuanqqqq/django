from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from manufacturer.models import Brand
from specifics.models import Memory, Color
# Create your models here.

class GPU(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=200)
    memory = models.ForeignKey(Memory, null=True, blank=True, on_delete=models.SET_NULL)
    color = models.ForeignKey(Color, null=True, blank=True, on_delete=models.SET_NULL)
    length = models.CharField(max_length=30, null=True, )
    TDP = models.IntegerField(null=True)

    def __str__(self):
        return self.brand.name + ' ' + self.model


