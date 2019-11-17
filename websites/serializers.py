from rest_framework import serializers
from .models import Website, User, Category


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
