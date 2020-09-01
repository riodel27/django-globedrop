from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    SUPER_ADMIN = 1
    NGO_ADMIN = 2
    USER = 3

    USER_TYPE_CHOIS = [
        (SUPER_ADMIN, 'Super Admin'),
        (NGO_ADMIN, 'NGO Admin'),
        (USER, 'Regular User')
    ]

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    language = models.CharField(max_length=250, null=True, blank=True)

    user_type = models.IntegerField(choices=USER_TYPE_CHOIS, default=USER)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    # TODO: relation with Organization

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
