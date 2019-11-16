from django.db import models
from django.utils import timezone

# Create your models here.


class Website(models.Model):
    url = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "website"
        verbose_name_plural = "websites"
        ordering = ["created_at"]

    def __str__(self):
        return self.url


class User(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.name