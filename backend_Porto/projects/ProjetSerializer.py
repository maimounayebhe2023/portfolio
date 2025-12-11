from rest_framework.serializers import ModelSerializer
from models import Projet

class ProjetSerializer(ModelSerializer):
    class meta:
        Model=Projet
        fields="__All__"
