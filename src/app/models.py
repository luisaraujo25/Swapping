from django.db import models
from django.utils import timezone

# Create your models here.

#USE TO TAKE DATA FROM THE DB

# class Student(models.Model):
#     up = models.CharField(max_length=11)
#     name = models.CharField(max_length=60)
#     email = models.EmailField(max_length=25)

#     def __str__(self):
#         return self.name

# class UC(models.Model):
#     name = models.CharField(max_length=40)
#     code = models.CharField(max_length=25)

#     def __str__(self):
#         return self.name

# class Class(models.Model):
#     number = models.IntegerField()
#     schedule = models.DateField(default=timezone.now)
#     studentID = models.ForeignKey("Student", on_delete=models.CASCADE)
#     ucID = models.ForeignKey("UC", on_delete=models.CASCADE)

#     def __str__(self):
#         return self.number

# class SwapRequest(models.Model):
#     date = models.DateField(default=timezone.now)
#     confirmation1 = models.BooleanField()
#     confirmation2 = models.BooleanField()
#     st1ID = models.ForeignKey("Student", on_delete=models.CASCADE, related_name = "request1", default = 0)
#     st2ID = models.ForeignKey("Student", on_delete=models.CASCADE, related_name = "request2", default = 0 )
#     ucID = models.ForeignKey("UC", on_delete=models.CASCADE)
#     st2up = models.IntegerField()
#     st2class = models.IntegerField()

#     def __str__(self):
#         return self.id


class Student(models.Model):
    up = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=25)

class UC(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=50, primary_key = True)

class StudentUC(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    uc = models.ForeignKey("UC", on_delete=models.CASCADE)
    class Meta:
        unique_together = (('student', 'uc'))

class Class(models.Model):
    code = models.IntegerField()
    number = models.IntegerField()

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
    confirmed1 = models.BooleanField()
    confirmed2 = models.BooleanField()
    date = models.DateField(auto_now=True)
    uc = models.ForeignKey("UC", on_delete=models.CASCADE)
    class1 = models.ForeignKey("Class", on_delete=models.CASCADE, related_name = "class1", default = 0)
    class1 = models.ForeignKey("Class", on_delete=models.CASCADE, related_name = "class2", default = 0)
    class Meta:
        unique_together = (('st1ID','st2ID'))