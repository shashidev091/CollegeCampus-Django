from django.db import models

# Create your models here.


class College(models.Model):
    college_name = models.CharField(max_length=100),
    grade = models.CharField(max_length=10)
    admission = models.CharField(max_length=255)
    course_duration = models.IntegerField()
    affiliation = models.CharField(max_length=255)
    placement = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    ranking = models.CharField(max_length=255)
    hostel = models.CharField(max_length=255)
    rating = models.IntegerField()
    admission_date = models.DateField()
    admission_till_date = models.DateField()

    def __str__(self):
        return f"""{{
            \"id\": {self.id},
            \"college_name\": {self.college_name},
            \"grade\": {self.grade},
            \"admission\": {self.admission},
            \"course_duration\": {self.course_duration},
            \"affiliation\": {self.affiliation},
            \"placement\": {self.placement},
            \"city\": {self.city},
            \"address\": {self.address},
            \"about\": {self.about},
            \"ranking\": {self.ranking},
            \"hostel\": {self.hostel},
            \"rating\": {self.rating},
            \"admission_date\": {self.admission_date},
            \"admission_till_date\": {self.admission_till_date},
        }}"""

    def get_dict(self):
        return {
            "id": self.id,
            "college_name": self.college_name,
            "grade": self.grade,
            "admission": self.admission,
            "course_duration": self.course_duration,
            "affiliation": self.affiliation,
            "placement": self.placement,
            "city": self.city,
            "address": self.address,
            "about": self.about,
            "ranking": self.ranking,
            "hostel": self.hostel,
            "rating": self.rating,
            "admission_date": self.admission_date,
            "admission_till_date": self.admission_till_date,
        }
