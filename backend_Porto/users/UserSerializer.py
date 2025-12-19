from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
import re
from rest_framework.validators import UniqueValidator

User=get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    """
    Serializer for the User model.

    This serializer handles the creation of new users and validation of input data.

    Fields:
    - username: required, unique if defined in the model
    - email: required, must be unique, validated by UniqueValidator
    """

    password=serializers.CharField(write_only=True, required=True)
    email=serializers.EmailField(required=True,
       validators=[UniqueValidator(queryset=User.objects.all(),message="This email is already in use." )]                          
    )
    class Meta:
        model=User
        fields='__all__'


    def validate_password(self, value):
        """
        Rules:
        - Minimum 8 characters
        - At least 1 uppercase
        - At least 1 lowercase
        - At least 1 number
        - At least 1 special character
        """
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>_]).{8,}$'

        if not re.match(pattern, value):
            raise serializers.ValidationError("Password must be at least 8 characters long, include one uppercase letter, one lowercase letter, one number, and one special character.")
        

        return value



    def create(self, validated_data):
        password=validated_data.pop('password')

        user=User(**validated_data)
        user.set_password(password)
        user.save()

        return user