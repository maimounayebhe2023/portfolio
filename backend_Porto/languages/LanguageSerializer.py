from rest_framework.serializers import ModelSerializer
from models import Language

class LanguageSerializer(ModelSerializer):

    class meta:
        model=Language
        fields="__All__"
