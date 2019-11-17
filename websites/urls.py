from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import (
    WebsiteViewSet,
    UserViewSet,
    CategoryViewSet,
)
router = DefaultRouter()
router.register(r'websites', WebsiteViewSet, base_name='websites')
router.register(r'users', UserViewSet, base_name='users')
router.register(r'categories', CategoryViewSet, base_name='categories')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]