from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields ='__all__'


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserAccount
        fields = '__all__'