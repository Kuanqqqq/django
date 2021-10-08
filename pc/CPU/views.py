from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_page(request):
    return HttpResponse('Hello')
    # return render(request, 'home_page.html')