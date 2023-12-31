"""Urls for venue app."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.venue, name='venue'),
    path('receive', views.receive, name='venue_receive'),
    path('undo/<id>', views.undo, name='venue_undo'),
    path('search', views.search, name='venue_search'),
    path('reports', views.reports, name='reports'),
    path('report1', views.report1, name='report1'),
    path('report2', views.report2, name='report2')
]