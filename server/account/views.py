from django.shortcuts import render
from account import serializers
from rest_framework import status, decorators,response, permissions

from rest_framework_simplejwt import views as jwt_views,serializers as jwt_serializers


@decorators.api_view(['POST'])
@decorators.permission_classes([])
def register(request):
    serializer = serializers.RegisterSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()
    return response.Response(status=status.HTTP_201_CREATED)


class AccountTokenObtainPairViewSerializer(jwt_serializers.TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        return token
    

class TokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = AccountTokenObtainPairViewSerializer


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def detail(request):
    serializer = serializers.AccountSerializer(request.user)
    return response.Response(serializer.data)