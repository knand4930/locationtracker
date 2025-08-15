import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=30, blank=True, null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        try:
            if not email:
                raise ValueError(_("The Email must be set"))
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            print(f"Error creating user: {str(e)}")

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(_("email address"), unique=True, max_length=200, blank=False, null=False)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = "email"
    username = None
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        ordering = ["-create_at"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_role(self):
        return getattr(self.user_role, "name", None)





class UserLocation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
