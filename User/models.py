from django.db import models
from django.utils import timezone, text
from django.urls import reverse

# Create your models here.


class Gender(models.TextChoices):
    M = "Male"
    F = "Female"
    O = "Other"


class User(models.Model):
    GENDER = {
        "M": "MALE",
        "F": "FEMALE",
        "O": "OTHER"
    }
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    profile_picture = models.ImageField()
    resume = models.FileField()
    gender = models.CharField(max_length=1, choices=GENDER)
    contact_no = models.CharField(max_length=10)

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=120)
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    # slug = models.SlugField(default="", null=False, db_index=True)

    def __str__(self):
        return f"""{{
            "id": {self.id},
            "first_name": {self.first_name},
            "last_name": {self.last_name},
            "middle_name": {self.middle_name},
            "age": {self.age},
            "email": {self.email},
            "profile_picture": {self.profile_picture},
            "resume": {self.resume},
            "gender": {self.gender},
            "contact_no": {self.contact_no},
            "username": {self.username},
            "is_active": {self.is_active},
            "created_at": {self.created_at},
            "updated_at": {self.updated_at}
        }}"""

    def get_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "middle_name": self.middle_name,
            "age": self.age,
            "email": self.email,
            "profile_picture": self.profile_picture.url if self.profile_picture else "no image",
            "resume": self.resume if self.resume else "No file",
            "gender": self.gender,
            "contact_no": self.contact_no,
            "username": self.username,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def get_absolute_url(self):
        return reverse("user_detail", args=[self.id])

    # def save(self, *args, **kwargs):
    #     self.slug = text.slugify(self.first_name, self.last_name)
    #     super().save(*args, **kwargs)


class Address(models.Model):
    village = models.CharField(max_length=255)
    street = models.CharField(max_length=100)
    tehsil = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal = models.IntegerField()
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    landline = models.CharField(max_length=11)

    def __str__(self):
        return {
            "village": self.village,
            "street": self.street,
            "tehsil": self.tehsil,
            "city": self.city,
            "postal": self.postal,
            "state": self.state,
            "country": self.country,
            "landline": self.landline
        }
