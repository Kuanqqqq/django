from django.db import models
from django.db.models.fields import CharField
from manufacturer.models import Brand
from specifics.models import Memory, Socket
from django.db.models.deletion import SET_NULL
# Create your models here.


class Series(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CoreCount(models.Model):
    count = models.IntegerField()

    def __str__(self):
        return self.count


class CoreClock(models.Model):
    clock = models.FloatField()
    unit = models.CharField(max_length=30)

    def __str__(self):
        return str(self.clock.__str__() + ' ' + self.unit)


class CPU(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, null=True, on_delete=models.SET_NULL)
    core_count = models.IntegerField(null=True)
    core_clock = models.ForeignKey(CoreClock, related_name='core_clock', null=True, on_delete=models.SET_NULL)
    boost_clock = models.ForeignKey(CoreClock, related_name='boost_clock', null=True, on_delete=models.SET_NULL)
    socket = models.ForeignKey(Socket, null=True, on_delete=models.SET_NULL)
    max_supported_memory = models.ForeignKey(Memory,null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.brand.name + ' ' + self.series.name



