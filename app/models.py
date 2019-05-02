from django.contrib.auth.models import Permission, User
from django.db import models


class Location(models.Model):
    user = models.CharField(max_length=100)
    location = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user + '-' + self.location


class Message(models.Model):
    user = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user