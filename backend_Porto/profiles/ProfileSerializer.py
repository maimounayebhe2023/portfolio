from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    # Display the portfolio URL instead of its ID
    portfolio = serializers.CharField(source='portfolio.access_url', read_only=True)
    class meta:
        model=Profile
        fields='__all__'