"""
users/urls.py

This module defines the URL routing for the User API endpoints using Django REST Framework.

It uses a DefaultRouter to automatically generate standard RESTful routes (list, create, update,  delete) for the UserViewSet.

"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
