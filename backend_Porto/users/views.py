from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .UserSerializer import UserSerializer

class UserListCreateAPIView(APIView):
    """
    APIView for listing and creating users.
    """
    #List all users
    def get(self, request, *args, **kwargs):       
        users=User.objects.all()
        serializer=UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK )
    
    #create a user
    def post(self,request, *args, **kwargs):
        serializer=UserSerializer(data=request.data)    
        if serializer.is_valid():
            user=serializer.save()
            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)