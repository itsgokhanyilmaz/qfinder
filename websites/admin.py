from django.contrib import admin
from .models import Website, User, Category, CheckingResult

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'created_at',
    ]

    list_filter = ['created_at']
    search_fields = ['name']

    class Meta:
        model = Category


class WebsiteAdmin(admin.ModelAdmin):

    list_display = [
        'url',
        'category',
        'created_at',
    ]

    list_filter = ['created_at']
    search_fields = ['url', 'category']

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

admin.site.register(User, UserAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CheckingResult)
