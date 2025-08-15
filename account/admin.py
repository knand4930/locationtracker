from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _

from .models import User, UserRole, UserLocation
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Custom admin for User model"""

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ("email", "is_staff", "is_active", "is_superuser", "date_joined", "last_login")
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ("email",)
    ordering = ("-create_at",)

    readonly_fields = ("date_joined", "last_login")  # ✅ Non-editable fields

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Permissions"), {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions", "user_role")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_active", "is_superuser"),
        }),
    )



@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    """Admin for user roles"""

    list_display = ("name", "create_at", "update_at")
    search_fields = ("name",)
    ordering = ("-create_at",)


@admin.register(UserLocation)
class UserLocationAdmin(admin.ModelAdmin):
    """Admin for user location"""

    list_display = ("user", "latitude", "longitude", "create_at", "update_at")
    search_fields = ("user__email", "latitude", "longitude")
    ordering = ("-create_at",)


# Optional: Register Permissions model for direct permission management in admin
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("name", "codename", "content_type")
    list_filter = ("content_type",)
    search_fields = ("name", "codename")
