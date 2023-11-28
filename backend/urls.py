"""
URL configuration for Backend app.
"""

from django.urls import path
from  . import views

urlpatterns = [
    path('', views.backend, name='backend'),
    path('search', views.search, name='back_search'),
    path('add', views.add, name='back_add'),
    path('save', views.save, name='back_save'),
]
