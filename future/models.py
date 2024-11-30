from django.db import models

from django.contrib.auth.models import AbstractUser


class Track(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    track = models.ForeignKey(Track, null=True, on_delete=models.SET_NULL)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'username']
