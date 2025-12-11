from rest_framework.serializers import ModelSerializer
from models import Skill

class SkillSerializer(ModelSerializer):

    class meta:
        model=Skill
        fields='__all__'