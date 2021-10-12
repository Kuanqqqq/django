from CPU import views
from django.urls import path

from .views import cpu

urlpatterns = [
     path('cpu/', cpu, name='cpu'),
]