from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    email=models.EmailField(unique=True)
    USERNAME_FIELD='email' # L'Email sera utlisé pour la connexion
    REQUIRED_FIELDS = ['username'] 
    def __str__(self):
        return self.email
