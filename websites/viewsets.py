from django.shortcuts import render
from rest_framework import generics

from .models import Websites
from .serializers import WebsitesSerializer


class ListWebsite(generics.ListCreateAPIView):

    # ListCreateAPIView is used for GET, POST requests
    queryset = Websites.objects.all()
    serializer_class = WebsitesSerializer


class DetailWebsite(generics.RetrieveUpdateDestroyAPIView):
    
    #  RetrieveUpdateDestroyAPIView is used for
    #  GET, PUT, PATCH and DELETE requests
    queryset = Websites.objects.all()
    serializer_class = WebsitesSerializer
