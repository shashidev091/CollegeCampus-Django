from django.db import models
from django.utils import timezone

# Create your models here.


class Gender(models.TextChoices):
    M = "Male"
    F = "Female"
    O = "Other"


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    profile_picture = models.ImageField()
    resume = models.FileField()
    gender = models.CharField(max_length=6, choices=Gender.choices)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField()
