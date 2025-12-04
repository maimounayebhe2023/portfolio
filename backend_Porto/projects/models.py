from django.db import models
from portfolio.models import Portfolio
# Create your models here
class Projet(models.Model):
    portfolio=models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projets/', null=True, blank=True)  
    lien = models.URLField(max_length=500, null=True, blank=True)  
    technologies = models.CharField(max_length=255)
    start_date=models.DateField
    end_date = models.DateField(null=True, blank=True)
    statut = models.CharField(
        max_length=50,
        choices=[('en_cours', 'En cours'), ('termine', 'Terminé')],
        default='en_cours'
    )

    def __str__(self):
        return self.titre
