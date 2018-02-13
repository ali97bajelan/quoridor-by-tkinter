from django.db import models


class UserPassword(models.Model):
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")
