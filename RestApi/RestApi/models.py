from django.db import models

class RestApi(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    