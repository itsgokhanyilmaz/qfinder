from django.db import models
from django.utils import timezone

# Create your models here.


class Websites(models.Model):
    url = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Website"
        verbose_name_plural = "Websites"
        ordering = ["created_at"]

    def __str__(self):
        return self.url