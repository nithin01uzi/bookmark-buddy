from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
