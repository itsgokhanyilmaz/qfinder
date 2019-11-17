from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["created_at"]

    def __str__(self):
        return self.name


class Website(models.Model):
    url = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "website"
        verbose_name_plural = "websites"
        ordering = ["created_at"]

    def __str__(self):
        return self.url


class User(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.name