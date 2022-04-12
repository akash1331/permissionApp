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

class dpSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserAccount
        fields = ('dp',)

class studentdetailSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserAccount
        fields = ('roll_no','first_name','last_name','parent_phone','student_phone',)