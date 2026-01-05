"""
users/urls.py

This module defines the URL routing for the User API endpoints using Django REST Framework.

It maps HTTP methods (GET, POST, etc.) to the corresponding methods of UserListCreateAPIView
for listing and creating users.
"""

from django.urls import path
from .views import UserListCreateAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
]
