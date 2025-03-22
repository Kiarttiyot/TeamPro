from django.urls import path
from . import views

urlpatterns = [
    path('ce01/', views.ce01s, name='ce01s'),
    path('ce02/', views.ce02s, name='ce02s'),
    path('ce03/', views.ce03s, name='ce03s'),
    path('ce04/', views.ce04s, name='ce04s'),
    path('ce01/<int:ce01D>', views.ce01, name='ce01'),
    path('ce02/<int:ce02D>', views.ce02, name='ce02'),
    path('ce03/<int:ce03D>', views.ce03, name='ce03'),
    path('ce04/<int:ce04D>', views.ce04, name='ce04'),
]
