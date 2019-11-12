from django.contrib import admin
from .models import Websites

# Register your models here.


class WebsiteAdmin(admin.ModelAdmin):

    list_display = [
        'url',
        'category',
        'created_at',
    ]

    list_filter = ['created_at']
    search_fields = ['category']

    class Meta:
        model = Websites