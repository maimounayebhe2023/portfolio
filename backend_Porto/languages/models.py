from django.db import models
from portfolio.models import Portfolio
# Create your models here.

class Language(models.Model):
    portfolio=models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)  
    proficiency = models.CharField(
        max_length=50,
        choices=[
            ('beginner', 'beginner'),
            ('intermediate', 'intermediate'),
            ('advanced', 'advanced'),
            ('native', 'native')
        ],
        default='beginner'
    )
