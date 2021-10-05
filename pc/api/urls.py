from django.urls import path
# from rest_framework.authtoken import views
from api import views


urlpatterns = [
    # path('auth/', views.obtain_auth_token, name='auth'),
    path('get_all_brands/', views.get_all_brands, name='get_all_brands')
]

# from django.conf.urls import url
# from rest_framework.authtoken import views as drf_views

# urlpatterns = [
#     url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
# ]
