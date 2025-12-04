from django.db import models
from portfolio.models import Portfolio

# Create your models here.

class WorkExperience(models.Model):
    portfolio=models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    job_title=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    start_date=models.DateField
    end_date=models.DateField(blank=True, null=True)
    is_current=models.BooleanField(default=False)
    description=models.TextField

    def __str__(self):
        return self.description