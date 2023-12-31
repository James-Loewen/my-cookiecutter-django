from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model, decorators

from apps.users.forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()

admin.site.login = decorators.login_required(admin.site.login)

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("preferred_name", "first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    list_display = [
        "email",
        "preferred_name",
        "first_name",
        "last_name",
        "is_superuser",
    ]
    search_fields = ["name"]
    ordering = ["id"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
