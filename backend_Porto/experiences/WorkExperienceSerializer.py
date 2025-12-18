from rest_framework import serializers
from .models import WorkExperience

class WorkExperienceSerializer(serializers.ModelSerializer):
    # Display the portfolio URL instead of its ID
    portfolio = serializers.CharField(source='portfolio.access_url', read_only=True)

    class Meta:
        model=WorkExperience
        fields='__all__'