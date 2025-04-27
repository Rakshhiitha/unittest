# App_UTG/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Default view for "Hello World"
    path('', views.hello_world, name='hello_world'),  # Root URL
    # The API endpoint for generating unit tests
    path('generate/', views.generate_tests, name='generate_tests'),
]
