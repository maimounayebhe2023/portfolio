from rest_framework.serializers import ModelSerializer
from models import WorkExperience

class WorkExperienceSerializer(ModelSerializer):

    class meta:
        model=WorkExperience
        fields='__all__'