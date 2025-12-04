from django.db import models
from portfolio.models import Portfolio
# Create your models here.

class PersonalInfo(models.Model):
    portfolio=models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    residence_address = models.CharField(max_length=500)
    linkedin = models.URLField(max_length=255, null=True, blank=True)
    github = models.URLField(max_length=255, null=True, blank=True)
    personal_website = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.full_name

