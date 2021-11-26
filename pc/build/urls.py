from django.urls import path
from .views import *

urlpatterns = [
     path('add_component/<str:name>/<int:pk>/', add_component, name='add_component'),
     path('delete_component/<str:name>/', delete_component, name='delete_component'),
]