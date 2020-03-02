from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Datasets(models.Model):
    title = models.CharField(max_length=100)
    date_updated = models.DateTimeField()
    frequency = models.CharField(max_length=50)
    file = models.FileField()

    def str(self):
        return self.title

