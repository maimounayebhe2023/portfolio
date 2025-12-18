from rest_framework import serializers
from .models import Projet

class ProjetSerializer(serializers.ModelSerializer):
    # Display the portfolio URL instead of its ID
    portfolio = serializers.CharField(source='portfolio.access_url', read_only=True)
    class Meta:
        Model=Projet
        fields="__All__"
