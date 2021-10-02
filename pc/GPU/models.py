from django.db import models
from django.db.models.base import Model
from manufacturer.models import Brand
from specifics.models import Memory
# Create your models here.

class GPU(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=200)
    memory = models.ForeignKey(Memory, null=True, blank=True, on_delete=models.CASCADE)
    # memory = models.ForeignKey(Memory, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand.name + ' ' + self.model


