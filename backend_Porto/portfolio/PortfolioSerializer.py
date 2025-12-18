from rest_framework import serializers
from .models import Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
     # Display the user instead of its ID
    user = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model=Portfolio
        fields = ['user', 'access_url', 'created_at']
        read_only_fields = ['created_at']
