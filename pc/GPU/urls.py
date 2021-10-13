from .views import gpu
from django.urls import path

urlpatterns = [
    path('gpu/', gpu, name='gpu'),
]