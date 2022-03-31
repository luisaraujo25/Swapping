from django.db import models
import datetime

# Create your models here.

#USE TO TAKE DATA FROM THE DB

class Student(models.Model):
    up = models.CharField(max_length=11)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=25)

class UC(models.Model):
    name = models.CharField(max_length=40)

class Class(models.Model):
    number = models.IntegerField()
    # schedule = truncate_date(self, models.DateField())

    # def truncate_date(self, dt):
    #     return dt - timedelta(days=dt.weekday())

class SwapRequest(models.Model):
    date = models.DateField()
    date = models.DateField(auto_now_add = True)