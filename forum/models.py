from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

class question(models.Model):
    ques = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.ques

class answer(models.Model):
    ans = models.CharField(max_length=5000)
