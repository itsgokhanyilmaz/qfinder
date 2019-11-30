from rest_framework import serializers
from .models import Website, User, Category, CheckingResult


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'name', 'created_at')
        model = Category


class WebsiteSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        fields = ('id', 'url', 'category', 'created_at')
        model = Website


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'name')
        model = User


class CheckingResultSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'url', 'is_available')
        model = CheckingResult