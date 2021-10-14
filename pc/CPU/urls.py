from CPU import views
from django.urls import path

from .views import cpu, get_all_cpus

urlpatterns = [
     path('cpu/', cpu, name='cpu'),
     path('get_all_cpus/', get_all_cpus, name='get_all_cpus'),
]