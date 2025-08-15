from django.urls import path

from account.views import UserListAPIView, UserRoleListAPIView, UserLocationListAPIView

urlpatterns=[
    path("user/list/", UserListAPIView.as_view(), name="UserListAPIView"),
    path("user/role/list/", UserRoleListAPIView.as_view(), name="UserRoleListAPIView"),
    path("user/location/list/", UserLocationListAPIView.as_view(), name="UserLocationListAPIView"),
]