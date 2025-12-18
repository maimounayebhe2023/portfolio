from django.db import models
from portfolio.models import Portfolio

# Create your models here.
class Profile(models.Model):
    portfolio=models.OneToOneField(Portfolio, on_delete=models.CASCADE)
    bio=models.CharField(max_length=150)
    job_title=models.TextField()
    profile_picture=models.ImageField(upload_to='profiles_picture', null=True, blank=True)

    def __str__(self):
        return self.bio