from django.contrib import admin
from .models import Website, User

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
        model = Website


class UserAdmin(admin.ModelAdmin):

    list_display = [
        'name',
    ]
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = User