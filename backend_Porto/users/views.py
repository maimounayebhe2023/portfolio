from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .UserSerializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User model.

    Provides CRUD operations:
    - create: POST /users/ → create a new user
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
