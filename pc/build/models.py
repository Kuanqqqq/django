from django.db import models
from CPU.models import CPU
from GPU.models import  GPU

# Create your models here.
class Build(models.Model):
    user_token = models.CharField(max_length=10)
    cpu = models.ForeignKey(CPU, null=True, blank=True, on_delete=models.CASCADE)
    gpu = models.ForeignKey(GPU, null=True, blank=True, on_delete=models.CASCADE)