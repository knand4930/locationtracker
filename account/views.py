from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from account.filterset import UserLocationFilterSet, UserFilterSet
from account.models import UserRole, UserLocation
from account.serializers import UserRoleSerializer, UserLocationSerializer, UserLitSerializer

User = get_user_model()
# Create your views here.


class UserRoleListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRoleSerializer
    queryset = UserRole.objects.all()

class UserLocationListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLocationSerializer
    queryset = UserLocation.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserLocationFilterSet

class UserListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLitSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilterSet
