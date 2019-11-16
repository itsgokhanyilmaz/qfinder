from rest_framework import serializers

from .models import Website, User

class WebsiteSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'url', 'category', 'created_at')
        model = Website


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'name')
        model = User