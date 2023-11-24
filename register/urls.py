"""
URL configuration for Register app.
"""

from django.urls import path
from  . import views

urlpatterns = [
    path('', views.register, name='register'),
]
