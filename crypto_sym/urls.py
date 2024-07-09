from django.urls import path
from . import views

urlpatterns = [

    path('index', views.index, name='index'),
path('index2', views.index2, name='index2'),
    path('', views.home, name='home'),
    path('data/', views.validate_params, name='validate_params'),
path('data2/', views.validate_params_aes, name='validate_params_aes'),
]