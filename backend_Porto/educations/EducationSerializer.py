from rest_framework.serializers import ModelSerializer
from models import Educations

class EducationSerializer(ModelSerializer):

    class meta:
        model=Educations
        fields='__All__'