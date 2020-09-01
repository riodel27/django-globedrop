from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


# TODO: how to modify admin for Accounts/Users

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'name', 'user_type',
                    'language', 'created_at', 'updated_at')
    ordering = ['created_at']


admin.site.register(User, CustomUserAdmin)
