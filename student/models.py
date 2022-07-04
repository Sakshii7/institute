from django.db import models


# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    roll_number = models.CharField(max_length=20)
    date = models.DateTimeField('date published', auto_now_add=True)


class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=50)

