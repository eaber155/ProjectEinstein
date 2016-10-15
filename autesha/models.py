from django.db import models
from django.utils import timezone

class Staff (models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name

