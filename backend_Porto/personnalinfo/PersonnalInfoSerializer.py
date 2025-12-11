from rest_framework.serializers import ModelSerializer
from models import PersonalInfo

class PersonalInfoSerializer(ModelSerializer):
    class meta:
        model=PersonalInfo
        fields="__All__"