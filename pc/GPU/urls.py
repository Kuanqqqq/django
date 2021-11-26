from .views import *
from django.urls import path

urlpatterns = [
    path('gpu/', gpu, name='gpu'),
    path('get_all_gpus/', get_all_gpus, name='get_all_gpus'),
]