from django.db import models    
from portfolio.models import Portfolio
# Create your models here.
class Hobby(models.Model):
    portfolio=models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 
    description = models.TextField(blank=True, null=True)  
