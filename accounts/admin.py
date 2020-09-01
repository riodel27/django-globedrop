from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


# TODO: how to modify admin for Accounts/Users

class CustomUserAdmin(UserAdmin):
    model = User
    list_dispay = ['email', 'name']


admin.site.register(User, CustomUserAdmin)
