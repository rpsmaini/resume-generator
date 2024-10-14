# profiles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_profile, name='create_profile'),  # Route for the profile form
]
