from django.db import models
from users.models import User

# Create your models here.
class Portfolio (models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    access_url=models.URLField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True )
    updated_at=models.DateTimeField(auto_now_add=True, auto_now=True )
    def __str__(self):
        return self.access_url