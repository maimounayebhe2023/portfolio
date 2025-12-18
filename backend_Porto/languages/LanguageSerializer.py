from rest_framework import serializers
from .models import Language

class LanguageSerializer(serializers.ModelSerializer):
    # Display the portfolio URL instead of its ID
    portfolio = serializers.CharField(source='portfolio.access_url', read_only=True)
    class Meta:
        model=Language
        fields='__all__'
