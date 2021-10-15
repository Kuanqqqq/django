from django.db import models
from django.db.models.fields import CharField
from specifics.models import TDP
# from manufacturer.models import Brand
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


class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class IntegratedGraphics(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CPU(models.Model):
    image = models.ImageField(upload_to='', blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=30, null=True)
    core_count = models.IntegerField(null=True)
    core_clock = models.ForeignKey(CoreClock, related_name='core_clock', null=True, on_delete=models.SET_NULL)
    boost_clock = models.ForeignKey(CoreClock, related_name='boost_clock', null=True, on_delete=models.SET_NULL)
    tdp = models.ForeignKey(TDP, null=True, on_delete=models.SET_NULL)
    integrated_graphics = models.ForeignKey(IntegratedGraphics, null=True, on_delete=models.SET_NULL)
    smt = models.BooleanField(default=False)
    socket = models.ForeignKey(Socket, null=True, on_delete=models.SET_NULL)
    max_supported_memory = models.ForeignKey(Memory,null=True, on_delete=models.SET_NULL)

    def table_name(self):
        return self.brand.name + ' ' + self.series

    def __str__(self):
        return self.brand.name + ' ' + self.series + ' ' + self.core_clock.__str__() + ' ' + str(self.core_count) + '-' + 'Core Processor'



