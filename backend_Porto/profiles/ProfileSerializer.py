from rest_framework.serializers import ModelSerializer
from models import Profiles

class ProfileSerializer(ModelSerializer):
    class meta:
        model=Profiles
        fields="__All__"