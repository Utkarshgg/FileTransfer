from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   
    path('', views.transfer_file, name='transfer_file'),
    
]