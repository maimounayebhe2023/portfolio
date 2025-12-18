from rest_framework import serializers
from .models import Hobby

class HobbySerializer(serializers.ModelSerializer):
    # Display the portfolio URL instead of its ID
    portfolio = serializers.CharField(source='portfolio.access_url', read_only=True)
    class Meta:
        model=Hobby
        fields='__all__'