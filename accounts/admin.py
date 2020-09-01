from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


# TODO: how to modify admin for Accounts/Users

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'name', 'user_type',
                    'language', 'created_at', 'updated_at')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': (
            'name', )}),
        (_('Additional info'), {'fields': (
            "language", "user_type", )
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'email', 'password1', 'password2', 'language', 'user_type'), }),)

    ordering = ['created_at']


admin.site.register(User, CustomUserAdmin)
