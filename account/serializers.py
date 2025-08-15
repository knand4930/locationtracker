from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as UserRegisterSerializer, UserSerializer as UserDetailsSerializer
from .models import UserRole, UserLocation
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(UserRegisterSerializer):
    class Meta:
        model = User
        fields = ('password', 'email', 'first_name', 'last_name', "user_role")

class UserSerializer(UserDetailsSerializer):
    class Meta:
        model = User
        fields = ("id",'email', 'first_name', 'last_name', "user_role", "get_role")


class UserLitSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",'email', 'first_name', 'last_name', "user_role", "get_role")


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ("id", "name")

class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = ("id", "user", "latitude", "longitude")


