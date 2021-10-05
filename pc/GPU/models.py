from django.db import models
from django.db.models.deletion import SET_NULL
from manufacturer.models import Brand
from specifics.models import Memory, Color, TDP
# Create your models here.


class Chipset(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.brand.name


class CoreClock(models.Model):
    clock = models.FloatField()
    unit = models.CharField(max_length=30)

    def __str__(self):
        return self.clock + ' ' + self.unit


class GPU(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    memory = models.ForeignKey(Memory, null=True, blank=True, on_delete=models.SET_NULL)
    color = models.ForeignKey(Color, null=True, blank=True, on_delete=models.SET_NULL)
    length = models.CharField(max_length=30, null=True, )
    TDP = models.ForeignKey(TDP, null=True, on_delete=models.SET_NULL)
    core_clock = models.ForeignKey(CoreClock, related_name='core_clock', null=True, on_delete=models.SET_NULL)
    boost_clock = models.ForeignKey(CoreClock, related_name='boost_clock', null=True, on_delete=models.SET_NULL)
    chipset = models.ForeignKey(Chipset, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.brand.name + ' ' + self.chipset.name
