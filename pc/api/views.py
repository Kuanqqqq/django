from django.shortcuts import render
from manufacturer.models import Brand
# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.core import serializers


def get_all_brands(request):
    brand_lst = Brand.objects.all()
    # data = serializers.serialize('xml', Brand.objects.all(), fields=('name'))
    return HttpResponse(brand_lst)