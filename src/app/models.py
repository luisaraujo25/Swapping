from django.db import models

# Create your models here.

#USE TO TAKE DATA FROM THE DB

class Request(models.Model):
    name = models.CharField(max_length=40)