from rest_framework.serializers import ModelSerializer
from models import Portfolio

class PortfolioSerializer(ModelSerializer):
    class meta:
        model=Portfolio
        fields="__All__"