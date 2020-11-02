from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Business_centres(models.Model):
    centre_name = models.CharField(max_length=20)
    contact_info = models.CharField(max_length=20)
    emergency_service = models.BooleanField(default=False)

    def __str__(self):
        return self.centre_name

    def save_centre(self):
        self.save()

    def delete_centre(self):
        self.delete()

class Neighbourhood(models.Model):
    name = models.CharField(max_length=20)
    centres = models.ManyToManyField(Business_centres)

    def __str__(self):
        return self.name

    def save_Neighbourhood(self):
        self.save()

    def delete_Neighbourhood(self):
        self.delete()class Neighbourhood(models.Model):
    name = models.CharField(max_length=20)
    centres = models.ManyToManyField(Business_centres)

    def __str__(self):
        return self.name

    def save_Neighbourhood(self):
        self.save()

    def delete_Neighbourhood(self):
        self.delete()
