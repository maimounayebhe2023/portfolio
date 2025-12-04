from django.db import models
from portfolio.models import Portfolio
#create here your models

class Educations(models.Model):
    portfolio=models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    institution=models.CharField(max_length=50)
    degree=models.CharField(max_length=50)
    field_of_study=models.CharField(max_length=50)
    education_type=models.CharField(max_length=20, 
        choices=[('online', 'online'),
            ('in_person', 'in_person')
        ],
        default='in_person'
    )
    start_date=models.DateField
    end_date=models.DateField(blank=True, null=True)
    is_current=models.BooleanField(default=False)
    grade=models.CharField(max_length=50, blank=True, null=True)
    description=models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.field_of_study