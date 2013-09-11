from django.db import models

class Idea(models.Model):
    text = models.CharField(max_length=150)

class Responses(models.Model):
    text = models.CharField(max_length=100)
