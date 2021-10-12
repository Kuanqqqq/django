from django.http.response import HttpResponse
from django.shortcuts import render
from .models import CPU
# Create your views here.

def cpu(request):
    #need to make the table to dynamic
    cpu_lst = CPU .objects.all()
    return render(request, 'cpu/cpu.html', {'cpu_lst': cpu_lst})