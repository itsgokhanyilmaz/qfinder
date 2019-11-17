from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    Website, 
    User, 
    Category,
    CheckingResult,
)
from .serializers import WebsiteSerializer, UserSerializer, CategorySerializer

import requests
from utils import exceptions
import django_filters
from django_filters import rest_framework as filters


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class WebsiteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `check_username` action.
    """
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    lookup_field = 'id'


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(field_name="name", lookup_expr='gte')
    
    class Meta:
        model = User
        fields = ['username']

class  UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter

    def perform_create(self, serializer):
        username = serializer.validated_data["name"]
        result = []
        queryset = Website.objects.all().values()
        
        for q in queryset:
            try:
                r = requests.get(q["url"]+"/{}".format(username))
                if r.status_code == 200:
                    print("OK {}".format(q["url"]))
                    CheckingResult.objects.create(name=username, url=q["url"], is_available=False)
                else:
                    print("NOK {}".format(q["url"]))
                    result.append(q["url"])
                    CheckingResult.objects.create(name=username, url=q["url"], is_available=True)
            except:
                exceptions.url_not_found_error()
        if len(result) > 0:
            serializer.save()
        else:
            raise ValueError("Avaliable user {} not found!".format(username))
