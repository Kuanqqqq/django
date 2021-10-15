from django.shortcuts import render
from CPU.models import CPU

def home_page(request):
    return render(request, 'home_page.html')


def list_page(request):
    return render(request, 'list.html')