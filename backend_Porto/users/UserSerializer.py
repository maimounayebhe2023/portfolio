from rest_framework.serializers import ModelSerializer
from models import User

class UserSerializer(ModelSerializer):

    class meta:
        model=User
        fields='__all__'