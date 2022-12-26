from django.db import models

# Create your models here.
class Employee(models.Model):
    POSTIONS_WORKER = 'W'
    POSTIONS_CASHER = 'C'
    POSTIONS_CLEANER = 'N'
    
    POSTIONS_CHOICES = [
        (POSTIONS_WORKER, 'Worker'),
        (POSTIONS_CASHER, 'Casher'),
        (POSTIONS_CLEANER,'Cleaner')]
    
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    ]
    name = models.CharField(max_length=255)
    age = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_MALE)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=1, choices=POSTIONS_CHOICES, default='W')
    salary = models.CharField(max_length=10)
    