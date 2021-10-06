from django.shortcuts import render
from manufacturer.models import Brand
from specifics.models import Memory
from django.http import JsonResponse, HttpResponse
from django.core import serializers


def get_all_brands(request):
    brand_lst = Brand.objects.all()
    return HttpResponse(brand_lst)

def get_all_memory(request):
    memory_lst = Memory.objects.all()
    return HttpResponse(memory_lst)
