from django.db import models

class Idea(models.Model):
    text = models.CharField(max_length=150)

    def __unicode__(self):
        return self.text

class Responses(models.Model):
    text = models.CharField(max_length=100)

    def __unicode__(self):
        return self.text
