from django.shortcuts import render

# Create your views here.
def gpu(request):
    return render(request, 'gpu/gpu.html')