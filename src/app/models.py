from django.db import models
from django.utils import timezone

# Create your models here.

#USE TO TAKE DATA FROM THE DB

class Student(models.Model):
    up = models.CharField(max_length=11)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=25)

    def __str__(self):
        return self.name

class UC(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Class(models.Model):
    number = models.IntegerField()
    schedule = models.DateField(default=timezone.now)
    studentID = models.ForeignKey("Student", on_delete=models.CASCADE)
    ucID = models.ForeignKey("UC", on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class SwapRequest(models.Model):
    date = models.DateField(default=timezone.now)
    confirmation1 = models.BooleanField()
    confirmation2 = models.BooleanField()
    st1ID = models.ForeignKey("Student", on_delete=models.CASCADE, related_name = "request1", default = 0)
    st2ID = models.ForeignKey("Student", on_delete=models.CASCADE, related_name = "request2", default = 0 )
    ucID = models.ForeignKey("UC", on_delete=models.CASCADE)
    st2up = models.IntegerField()
    st2class = models.IntegerField()

    def __str__(self):
        return self.id