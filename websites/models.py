from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["created_at"]

    def __str__(self):
        return self.name


class Website(models.Model):
    url = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Website"
        verbose_name_plural = "Websites"
        ordering = ["created_at"]

    def __str__(self):
        return self.url


class User(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name


class CheckingResult(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=150)
    is_available = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = "Check Result"
        verbose_name_plural = "Check Results"

    def __str__(self):
        return self.name + self.url
