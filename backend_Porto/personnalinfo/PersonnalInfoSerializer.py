from rest_framework import serializers
from .models import PersonalInfo

class PersonalInfoSerializer(serializers.ModelSerializer):
    # Display the portfolio URL instead of its ID
    portfolio = serializers.CharField(source='portfolio.access_url', read_only=True)
    class Meta:
        model=PersonalInfo
        fields='__all__'