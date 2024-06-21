from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True)

    def __str__(self):
        return f"{self.first_name}"
    