import django_filters
from django.contrib.auth import get_user_model
from account.models import UserLocation

User = get_user_model()

class UserLocationFilterSet(django_filters.FilterSet):
    user = django_filters.UUIDFilter(field_name="user")
    class Meta:
        model = UserLocation
        fields = ["user"]

class UserFilterSet(django_filters.FilterSet):
    user_role = django_filters.UUIDFilter(field_name="user_role")
    class Meta:
        model = User
        fields = ["user_role"]