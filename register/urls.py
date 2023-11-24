"""
URL configuration for Register app.
"""

from django.urls import path
from  . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('email', views.email, name='email'),
    path('new', views.new, name='register_new'),
    path('invited', views.invited, name='register_invited'),
    path('view/<id>', views.view, name='register_view'),
]
