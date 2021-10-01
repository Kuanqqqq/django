from django.db import models
from django.db.models.base import Model
from manufacturer.models import Brand
# Create your models here.

class GPU(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=200)

    def __str__(self):
        return self.brand.name + ' ' + self.model

