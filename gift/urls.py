"""End point for gift app"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.gift, name='gift'),
    path('search', views.search, name='gift_search'),
    path('issue', views.issue, name='gift_issue'),
]