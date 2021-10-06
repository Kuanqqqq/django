from django.urls import path
# from rest_framework.authtoken import views
from api import views


urlpatterns = [
    path('get_all_brands/', views.get_all_brands, name='get_all_brands'),
    path('get_all_memory/', views.get_all_memory, name='get_all_memory'),
]
