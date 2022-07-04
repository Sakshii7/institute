from django.db import models

# Create your models here.


class Staff(models.Model):
    Male = 'M'
    Female = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),
    )
    teacher_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=Male)
    qualification = models.CharField(max_length=30)
