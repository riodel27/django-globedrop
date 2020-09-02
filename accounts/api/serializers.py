
from rest_framework import generics, permissions, serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', "name", 'language', 'user_type',)
        # fields = '__all__'
