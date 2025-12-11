from rest_framework.serializers import ModelSerializer
from models import Hobby

class HobbySerializer(ModelSerializer):
    class meta:
        model=Hobby
        fields="__All__"