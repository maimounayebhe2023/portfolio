from django.db import models
from portfolio.models import Portfolio

# Create your models here.
from django.db import models

class Skill(models.Model):
    portfolio=models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    proficiency = models.CharField(
        max_length=50,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
            ('expert', 'Expert')
        ],
        default='beginner'
    )
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.proficiency})"
