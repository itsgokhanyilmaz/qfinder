from rest_framework import serializers

from .models import Websites

class WebsitesSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'url', 'category', 'created_at')
        model = Websites
