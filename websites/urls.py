from django.contrib import admin
from django.urls import path, include

from .viewsets import (
    ListWebsite,
    DetailWebsite,
)

urlpatterns = [

    path('websites', ListWebsite.as_view()),
    path('websites/<int:pk>', DetailWebsite.as_view()),

]