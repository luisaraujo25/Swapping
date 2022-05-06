from django.db import models
from django.utils import timezone

# Create your models here.

#USE TO TAKE DATA FROM THE DB

class Student(models.Model):
    up = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=25)

    # class Meta:
    #     constraints = [
    #     models.UniqueConstraint(fields=['upNumber'], name='unique_up')]

class UC(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['code'], name="codeUnique")
        ]

class StudentUC(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    uc = models.ForeignKey("UC", on_delete=models.CASCADE)
    class Meta:
        unique_together = (('student', 'uc'))

class Class(models.Model):
    number = models.IntegerField()
    code = models.CharField(max_length=50)

    def __str__(self):
        return str(self.number)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['number'], name="classNoUnique")
        ]

class ClassUC(models.Model):
    uc = models.ForeignKey("UC", on_delete=models.CASCADE)
    cl = models.ForeignKey("Class", on_delete=models.CASCADE)
    class Meta:
        unique_together = (('uc','cl'))


class ScheduleSlot(models.Model):
    weekDay = models.CharField(max_length=50)
    startTime = models.IntegerField()
    duration = models.IntegerField()
    typeClass = models.CharField(max_length=50) #Prática, Teórica, Lab
    classUC = models.ForeignKey("classUC", on_delete=models.CASCADE)

class Request(models.Model):
    st1ID = models.ForeignKey("Student", on_delete=models.CASCADE, related_name = "request1", default = 0)
    st2ID = models.ForeignKey("Student", on_delete=models.CASCADE, related_name = "request2", default = 0)
    confirmed1 = models.BooleanField(default = False)
    confirmed2 = models.BooleanField(default = False)
    date = models.DateField(auto_now_add=True)
    uc = models.ForeignKey("UC", on_delete=models.CASCADE)
    token1 = models.CharField(max_length=30, null=True)
    token2 = models.CharField(max_length=30, null=True)
    class1 = models.ForeignKey("Class", on_delete=models.CASCADE, related_name = "class1", default = 0)
    class2 = models.ForeignKey("Class", on_delete=models.CASCADE, related_name = "class2", default = 0)

    # class Meta:
    #     unique_together = (('st1ID','st2ID'))